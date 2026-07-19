from pathlib import Path
import subprocess
import re


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
            start_frame=0,
            frame_count=None,
            fps=25,
            progress=None
        ):

        destination_pattern = Path(destination_pattern)
        destination_pattern.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            "ffmpeg",

            "-progress", "pipe:1",
            "-nostats",
            "-y",

            "-i", str(source),

            "-ss", str(start_frame / fps),

            "-start_number", "1"
        ]

        if frame_count is not None:

            cmd.extend([
                "-frames:v",
                str(frame_count)
            ])

        cmd.append(str(destination_pattern))

        self.run_with_progress(
            cmd,
            progress
        )

        return sorted(destination_pattern.parent.glob("frame_*.png"))

    def encode_video(                
            self,
            input_pattern,
            output_file,
            video_info,
            config):

        encoder = self._get_encoder(config.codec)

        subprocess.run(
            [
                "ffmpeg",
                "-y",

                "-framerate",
                str(video_info.fps),

                "-i",
                str(input_pattern),

                "-c:v",
                encoder,

                "-preset",
                config.preset,

                "-crf",
                str(config.crf),

                "-pix_fmt",
                "yuv420p",

                str(output_file)
            ],
            check=True
        )


    def _get_encoder(self, codec: str):

        match codec:

            case "h264":
                return "libx264"

            case "hevc":
                return "libx265"

            case _:
                raise ValueError(
                    f"Códec no soportado: {config.codec}"
                )

    def concatenate_videos(
            self,
            videos,
            concat_file,
            output):

        concat_file = Path(concat_file)

        concat_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(concat_file, "w", encoding="utf8") as f:

            for video in videos:

                f.write(
                    f"file '{video.resolve()}'\n"
                )

        subprocess.run(

            [

                "ffmpeg",

                "-y",

                "-f", "concat",

                "-safe", "0",

                "-i", str(concat_file),

                "-c", "copy",

                str(output)

            ],

            check=True

        )

    def merge_audio(
            self,
            video,
            audios,
            output):

        cmd = [

            "ffmpeg",

            "-y",

            "-i",
            str(video)

        ]

        # Añadir todas las pistas de audio
        for audio in audios:

            cmd.extend([

                "-i",
                str(audio)

            ])

        # Seleccionar el vídeo
        cmd.extend([

            "-map",
            "0:v"

        ])

        # Seleccionar todas las pistas de audio
        for i in range(len(audios)):

            cmd.extend([

                "-map",
                f"{i + 1}:a"

            ])

        # Copiar sin recodificar
        cmd.extend([

            "-c:v",
            "copy",

            "-c:a",
            "copy",

            "-shortest",

            str(output)

        ])

        subprocess.run(
            cmd,
            check=True
        )

    def run_with_progress(self, command, progress=None):

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for line in process.stdout:

            line = line.strip()

            if progress and line.startswith("frame="):

                try:
                    frame = int(line.split("=")[1])
                    progress.update(frame)
                except ValueError:
                    pass

        process.wait()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(
                process.returncode,
                command
            )