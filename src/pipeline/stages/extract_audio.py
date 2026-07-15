from pipeline.stages.base import Stage

from video.ffmpeg import FFmpeg


class ExtractAudioStage(Stage):

    def __init__(self):
        self.ffmpeg = FFmpeg()

    def run(self, context):

        context.progress.step("Extrayendo audios...")

        context.audio_files = []

        sources = [
            context.config.input_file,
            *context.config.additional_audio_sources
        ]

        for index, source in enumerate(sources, start=1):

            destination = context.workspace.audio_track(index)

            self.ffmpeg.extract_audio(
                source,
                destination
            )

            context.audio_files.append(destination)

            context.progress.info(
                f"Audio {index} extraído: {destination}"
            )