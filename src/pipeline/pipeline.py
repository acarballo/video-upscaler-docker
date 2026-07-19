from pipeline.context import PipelineContext

from pipeline.stages.analyze import AnalyzeStage
from pipeline.stages.extract_audio import ExtractAudioStage
from pipeline.stages.process_blocks import ProcessBlocksStage
from pipeline.stages.merge_audio import MergeAudioStage
from pipeline.stages.concatenate_blocks import ConcatenateBlocksStage


class Pipeline:

    def __init__(self, config):

        self.context = PipelineContext(config)

        self.stages = [

            AnalyzeStage(),

            ExtractAudioStage(),

            ProcessBlocksStage(),

            ConcatenateBlocksStage(),

            MergeAudioStage()
        ]

    def run(self):

        for stage in self.stages:

            stage.run(self.context)