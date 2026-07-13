from common.logger import Logger

class Progress:

    def __init__(self):
        self.logger = Logger.get()

    def step(self, message):

        self.logger.info("")
        self.logger.info("=" * 60)
        self.logger.info(message)
        self.logger.info("=" * 60)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)