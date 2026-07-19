from video.ffmpeg import FFmpeg
from model.videoblock import VideoBlock

class VideoBlockProcessor:

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def create_blocks(self, context):

        total_frames = (
            context.config.max_frames
            or context.video_info.total_frames
        )

        block_size = context.config.block_size

        blocks = []

        index = 0

        first_frame = 0

        while first_frame < total_frames:

            frame_count = min(
                block_size,
                total_frames - first_frame
            )

            blocks.append(
                VideoBlock(
                    index=index,
                    first_frame=first_frame,
                    frame_count=frame_count
                )
            )

            index += 1
            first_frame += frame_count

        return blocks

    def process(self, context):

        context.blocks = self.create_blocks(context)

        # Comenzar desde el bloque indicado
        context.blocks = [
            block
            for block in context.blocks
            if block.index >= context.config.from_block
        ]

        # Limitar el número de bloques a procesar
        if context.config.block_count is not None:
            context.blocks = context.blocks[:context.config.block_count]

        context.progress.info(
            f"Se procesarán {len(context.blocks)} bloques."
        )

        context.progress.step(
            f"Procesando vídeo en bloques de "
            f"{context.config.block_size} fotogramas..."
        )

        for block in context.blocks:

            context.progress.info(
                f"Procesando bloque {block.index + 1}/{len(context.blocks)} "
                f"(frames {block.first_frame} - "
                f"{block.first_frame + block.frame_count - 1})"
            )

            output = context.workspace.encoded_block(block)

            if output.exists():

                context.progress.info(
                    f"Bloque {block.index + 1} ya existe. Se omite."
                )

                continue

            self.process_block(context, block)

            context.progress.info(
                f"Bloque {block.index + 1} finalizado."
            )


    def process_block(self, context, block):

        self.extract_frames(context, block)

        self.upscale(context, block)

        self.encode(context, block)

        if context.config.cleanup_blocks:
            context.workspace.clean_block(block)

            context.progress.info(
                f"Bloque {block.index + 1} limpiado."
            )


    def extract_frames(self, context, block):

        context.progress.start(
            total=block.frame_count,
            title=f"Extrayendo bloque {block.index}..."
        )

        context.frames = self.ffmpeg.extract_frames(
            context.workspace.input_video,
            context.workspace.frame_pattern(block),
            start_frame=block.first_frame,
            frame_count=block.frame_count,
            fps=context.video_info.fps,
            progress=context.progress
        )

        context.progress.finish()

        context.progress.info(
            f"{len(context.frames)} fotogramas extraídos."
        )

    def upscale(self, context, block):

        if context.upscaler is None:

            from ai.factory import UpscalerFactory

            context.progress.step(
                f"Inicializando {context.config.model.upper()}..."
            )

            context.upscaler = UpscalerFactory.create(
                context.config.model
            )

            context.upscaler.load()

            context.progress.info(
                f"{context.config.model.upper()} cargado correctamente."
            )

        context.progress.start(
            total=len(context.frames),
            title=f"Reescalando bloque {block.index}..."
        )

        destination_dir = context.workspace.upscaled_dir(block)

        images = [

            (
                frame,
                destination_dir / frame.name
            )

            for frame in context.frames

        ]

        context.upscaler.upscale_images(
            context,
            images
        )

        context.progress.finish()

        context.progress.info(
            f"Bloque {block.index} reescalado."
        )       

    def encode(self, context, block):

        context.progress.step("Codificando vídeo...")

        self.ffmpeg.encode_video(
            context.workspace.upscaled_pattern(block),
            context.workspace.encoded_block(block),
            context.video_info,
            context.config
        )

        context.progress.info(
            f"Bloque {block.index} codificado."
        )              