from pipeline.stages.base import Stage

from video.ffmpeg import FFmpeg


class ExtractAudioStage(Stage):

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def run(self, context):

        context.progress.step("Extrayendo audio...")

        self.ffmpeg.extract_audio(

            context.workspace.input_video,

            context.workspace.audio_file
        )