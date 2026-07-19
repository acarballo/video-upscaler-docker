import argparse

from config import Config
from common.logger import Logger
from pipeline.pipeline import Pipeline


def main():

    logger = Logger.get()

    parser = argparse.ArgumentParser()

    parser.add_argument("input_video")
    parser.add_argument("audio", nargs="*")

    parser.add_argument(
        "--from-block",
        type=int,
        default=0,
        help="Bloque desde el que comenzar el procesamiento."
    )

    parser.add_argument(
        "--block-count",
        type=int,
        help="Número máximo de bloques a procesar."
    )

    args = parser.parse_args()

    config = Config(
        input_file=args.input_video,
        output_file="salida.mkv",
        additional_audio_sources=args.audio,

        from_block=args.from_block,
        block_count=args.block_count
    )

    Pipeline(config).run()


if __name__ == "__main__":
    main()