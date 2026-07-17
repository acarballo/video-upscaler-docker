from video.ffmpeg import FFmpeg


class VideoBlockProcessor:

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def extract_frames(self, context):

        context.progress.start(
            total=context.config.max_frames,
            title="Extrayendo fotogramas..."
        )

        context.frames = self.ffmpeg.extract_frames(
            context.workspace.input_video,
            context.workspace.frame_pattern,
            max_frames=context.config.max_frames,
            progress=context.progress
        )

        context.progress.finish()

        context.progress.info(
            f"{len(context.frames)} fotogramas extraídos."
        )

    def upscale(self, context):

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
            title="Reescalando fotogramas..."
        )

        images = [
            (
                frame,
                context.workspace.upscaled / frame.name
            )
            for frame in context.frames
        ]

        context.upscaler.upscale_images(
            context,
            images
        )

        context.progress.finish()

        context.progress.info(
            "Reescalado finalizado."
        )        

    def encode(self, context):

        context.progress.step("Codificando vídeo...")

        self.ffmpeg.encode_video(
            context.workspace.upscaled_pattern,
            context.workspace.encoded_video,
            context.video_info,
            context.config
        )

        context.encoded_video = context.workspace.encoded_video

        context.progress.info(
            f"Vídeo codificado: {context.encoded_video}"
        )                