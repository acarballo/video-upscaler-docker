from pathlib import Path
from common.logger import Logger
import subprocess


class FFmpeg:
   

    def extract_audio(self, info, destination):

        logger = Logger.get()

        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info("Extrayendo audio...")

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                info.filename,
                "-vn",
                "-acodec",
                "copy",
                str(destination)
            ],
            check=True
        )

        return destination


    def extract_frames(self, info, destination):

        logger = Logger.get()

        destination = Path(destination)
        destination.mkdir(parents=True, exist_ok=True)

        output = destination / "frame_%08d.png"

        logger.info("Extrayendo fotogramas...")

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                info.filename,
                str(output)
            ],
            check=True
        )

        return destination