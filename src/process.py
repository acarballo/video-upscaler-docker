import sys

from config import Config
from common.logger import Logger

from pipeline.pipeline import Pipeline


def main():

    logger = Logger.get()

    if len(sys.argv) < 2:
        logger.error(
            "Uso: python process.py <video> [audio1] [audio2] ..."
        )
        sys.exit(1)

    config = Config(
        input_file=sys.argv[1],
        additional_audio_sources=sys.argv[2:],
        output_file="salida.mkv",
        max_frames=100
    )

    Pipeline(config).run()


if __name__ == "__main__":
    main()