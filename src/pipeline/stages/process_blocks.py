from pipeline.stages.base import Stage

from pipeline.processor.video_block_processor import VideoBlockProcessor


class ProcessBlocksStage(Stage):

    def __init__(self):

        self.processor = VideoBlockProcessor()

    def run(self, context):

        self.processor.process(context)