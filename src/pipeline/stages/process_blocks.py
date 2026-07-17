from pipeline.stages.base import Stage

from pipeline.processor.video_block_processor import VideoBlockProcessor

from pipeline.stages.extract_frames import ExtractFramesStage
from pipeline.stages.upscale import UpscaleStage
from pipeline.stages.encode_video import EncodeVideoStage


class ProcessBlocksStage(Stage):

    def __init__(self, model):

        self.processor = VideoBlockProcessor()

        self.extract = ExtractFramesStage()
        self.upscale = UpscaleStage(model)
        self.encode = EncodeVideoStage()

    def run(self, context):

        self.processor.extract_frames(context)
        self.processor.upscale(context)
        self.encode.run(context)

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