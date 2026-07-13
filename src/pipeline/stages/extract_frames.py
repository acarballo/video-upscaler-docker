from pipeline.stages.base import Stage

from video.ffmpeg import FFmpeg


class ExtractFramesStage(Stage):

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def run(self, context):

        context.progress.step("Extrayendo fotogramas...")

        context.frames = self.ffmpeg.extract_frames(

            context.workspace.input_video,

            context.workspace.frame_pattern,

            max_frames=1000
        )

        context.progress.info(
            f"{len(context.frames)} fotogramas extraídos."
        )