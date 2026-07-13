from pipeline.stages.base import Stage

from video.detector import VideoDetector
from workspace import Workspace


class AnalyzeStage(Stage):

    def __init__(self):

        self.detector = VideoDetector()

    def run(self, context):

        context.progress.step("Analizando vídeo...")

        context.video_info = self.detector.analyze(
            context.config.input_file
        )

        context.workspace = Workspace(
            context.video_info
        )

        context.progress.info("")
        context.progress.info(context.video_info)