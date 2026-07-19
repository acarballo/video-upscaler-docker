from pipeline.stages.base import Stage

from video.ffmpeg import FFmpeg


class ConcatenateBlocksStage(Stage):

    def __init__(self):

        self.ffmpeg = FFmpeg()

    def run(self, context):

        context.progress.step(
            "Concatenando bloques..."
        )

        videos = context.workspace.encoded_blocks()

        context.progress.info(
            f"Concatenando {len(videos)} bloques..."
        )

        self.ffmpeg.concatenate_videos(

            videos,

            context.workspace.concat_list,

            context.workspace.concatenated_video

        )

        context.encoded_video = (
            context.workspace.concatenated_video
        )

        context.progress.info(
            "Bloques concatenados."
        )