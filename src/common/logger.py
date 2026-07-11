import logging
import sys


class Logger:

    _configured = False

    @classmethod
    def get(cls):

        if cls._configured:
            return logging.getLogger("video-ai")

        logger = logging.getLogger("video-ai")

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            "%H:%M:%S"
        )

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        cls._configured = True

        return logger