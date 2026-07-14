from pipeline.stages.base import Stage

from video.ffmpeg import FFmpeg


class EncodeVideoStage(Stage):

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def run(self, context):

        context.progress.step("Codificando vídeo...")

        self.ffmpeg.encode_video(
            context.workspace.upscaled_pattern,
            context.workspace.encoded_video,
            context.video_info,
            context.config
        )

        context.encoded_video = context.workspace.encoded_video

        context.progress.info(
            f"Vídeo generado: {context.encoded_video}"
        )