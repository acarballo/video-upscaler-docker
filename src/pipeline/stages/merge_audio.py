from pipeline.stages.base import Stage

from video.ffmpeg import FFmpeg


class MergeAudioStage(Stage):

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def run(self, context):

        context.progress.step("Combinando vídeo y audio...")

        self.ffmpeg.merge_audio(

            context.encoded_video,

            context.audio_file,

            context.workspace.output_video

        )

        context.output_video = context.workspace.output_video

        context.progress.info(

            f"Vídeo final: {context.output_video}"

        )