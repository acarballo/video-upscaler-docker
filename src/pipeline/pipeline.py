from pipeline.context import PipelineContext

from pipeline.stages.analyze import AnalyzeStage
from pipeline.stages.extract_audio import ExtractAudioStage
from pipeline.stages.extract_frames import ExtractFramesStage
from pipeline.stages.upscale import UpscaleStage
from pipeline.stages.encode import EncodeStage


class Pipeline:

    def __init__(self, config):

        self.context = PipelineContext(config)

        self.stages = [

            AnalyzeStage(),

            ExtractAudioStage(),

            ExtractFramesStage(),

            UpscaleStage(config.model),

            EncodeStage()

        ]

    def run(self):

        for stage in self.stages:

            stage.run(self.context)