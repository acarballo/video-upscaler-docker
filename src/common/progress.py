import time

from common.logger import Logger


class Progress:

    def __init__(self):

        self.logger = Logger.get()

        self.total = 0
        self.current = 0
        self.start_time = None
        self.width = 40

    def step(self, text):

        self.logger.info("")
        self.logger.info("=" * 60)
        self.logger.info(text)
        self.logger.info("=" * 60)

    def info(self, text):

        self.logger.info(text)

    def start(self, total, title=None):

        self.total = total
        self.current = 0
        self.start_time = time.time()

        if title:
            self.step(title)

    def increment(self):

        self.update(self.current + 1)

    def update(self, current):

        self.current = current

        percent = self.current / self.total

        filled = int(percent * self.width)

        bar = "█" * filled + "░" * (self.width - filled)

        elapsed = time.time() - self.start_time

        fps = self.current / elapsed if elapsed else 0

        eta = (self.total - self.current) / fps if fps else 0

        print(
            f"\r[{bar}] "
            f"{percent*100:5.1f}% "
            f"{self.current}/{self.total} "
            f"{fps:.2f} img/s "
            f"ETA {eta:6.0f}s",
            end="",
            flush=True
        )

    def finish(self):

        elapsed = time.time() - self.start_time

        print()

        self.logger.info(
            f"Finalizado en {elapsed:.1f} segundos."
        )