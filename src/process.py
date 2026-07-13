import sys

from config import Config
from common.logger import Logger

from pipeline.pipeline import Pipeline


def main():

    logger = Logger.get()

    if len(sys.argv) != 2:
        logger.error("Uso: python process.py <video>")
        sys.exit(1)

    config = Config(
        input_file=sys.argv[1],
        output_file="salida.mkv"
    )

    Pipeline(config).run()


if __name__ == "__main__":
    main()