import logging


class TestLogger:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def info(self, msg, *args):
        self.logger.info(msg, *args)

    def error(self, msg, *args):
        self.logger.error(msg, *args)


test_logger = TestLogger()
