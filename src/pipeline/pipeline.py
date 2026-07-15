from pipeline.context import PipelineContext

from pipeline.stages.analyze import AnalyzeStage
from pipeline.stages.extract_audio import ExtractAudioStage
from pipeline.stages.extract_frames import ExtractFramesStage
from pipeline.stages.upscale import UpscaleStage
from pipeline.stages.encode_video import EncodeVideoStage
from pipeline.stages.merge_audio import MergeAudioStage


class Pipeline:

    def __init__(self, config):

        self.context = PipelineContext(config)

        self.stages = [

            AnalyzeStage(),

            ExtractAudioStage(),

            # ExtractFramesStage(),

            # UpscaleStage(config.model),

            EncodeVideoStage(),

            MergeAudioStage()

        ]

    def run(self):

        for stage in self.stages:

            stage.run(self.context)