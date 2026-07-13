from pathlib import Path
import subprocess


class FFmpeg:

    def extract_audio(self, source, destination):

        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(source),
                "-vn",
                "-acodec",
                "copy",
                str(destination)
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

    def extract_frames(
            self,
            source,
            destination_pattern,
            max_frames=None):

        destination_pattern = Path(destination_pattern)
        destination_pattern.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            str(source)
        ]

        if max_frames is not None:
            cmd.extend([
                "-frames:v",
                str(max_frames)
            ])

        cmd.append(str(destination_pattern))

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        return sorted(destination_pattern.parent.glob("frame_*.png"))

    def encode_video(self, input_pattern, output_file, fps):

        subprocess.run(
            [
                "ffmpeg",
                "-y",

                "-framerate", str(fps),

                "-i", str(input_pattern),

                "-c:v", "libx264",

                "-pix_fmt", "yuv420p",

                str(output_file)
            ],
            check=True
        )