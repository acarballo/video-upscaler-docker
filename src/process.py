import sys

from config import Config
from common.logger import Logger

from video.detector import VideoDetector
from video.ffmpeg import FFmpeg

from workspace import Workspace

from ai.factory import UpscalerFactory
import time


def main():

    logger = Logger.get()

    if len(sys.argv) != 2:
        logger.error("Uso: python process.py <video>")
        sys.exit(1)

    video = sys.argv[1]

    config = Config(
        input_file=video,
        output_file="salida.mkv"
    )

    logger.info("Analizando vídeo...")

    detector = VideoDetector()
    info = detector.analyze(config.input_file)

    logger.info("")
    logger.info(info)

    workspace = Workspace(info)

    ffmpeg = FFmpeg()

    logger.info("Extrayendo audio...")

    ffmpeg.extract_audio(
        workspace.input_video,
        workspace.audio_file
    )

    logger.info("Extrayendo fotogramas...")

    frames = ffmpeg.extract_frames(
        workspace.input_video,
        workspace.frame_pattern,
        max_frames=1
    )

    logger.info(f"{len(frames)} fotogramas extraídos.")
   
    logger.info("Inicializando motor IA...")

    upscaler = UpscalerFactory.create(config.model)
    upscaler.load()

    logger.info("Reescalando primer fotograma...")

    first_frame = frames[0]

    output_frame = workspace.upscaled / first_frame.name

    start = time.time()

    upscaler.upscale_image(
        first_frame,
        output_frame
    )

    elapsed = time.time() - start

    logger.info(f"Escalado completado en {elapsed:.2f} segundos")

    logger.info(f"Generado {output_frame}")

if __name__ == "__main__":
    main()