import subprocess


class FFmpeg:

    def extract_audio(self, source, destination):

        subprocess.run([

            "ffmpeg",

            "-y",

            "-i",

            source,

            "-vn",

            "-acodec",

            "copy",

            destination

        ], check=True)


    def extract_frames(self, source, output_pattern):

        subprocess.run([

            "ffmpeg",

            "-y",

            "-i",

            source,

            output_pattern

        ], check=True)