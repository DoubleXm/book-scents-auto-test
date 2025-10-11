from utils.config import config
from pathlib import Path
import logging


class Logger:
    def __init__(
        self,
        name="book_scents_test",
        log_level=config.LOG_LEVEL,
        console_output=config.CONSOLE_OUTPUT,
        file_output=config.FILE_OUTPUT,
        log_dir=config.LOG_DIR,
        max_bytes=1024 * 1024 * 10,
        backup_count=5,
    ):
        self.name = name
        self.log_level = log_level
        self.console_output = console_output
        self.file_output = file_output
        self.log_dir = Path(log_dir)
        self.max_bytes = max_bytes
        self.backup_count = backup_count

        # 创建 logger 目录
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.log_level)

        formatter = self._create_log_formatter()
        if self.console_output:
            self.logger.addHandler(self._create_console_handler())
        if self.file_output:
            self.logger.addHandler(self._create_file_handler())

    def _create_log_formatter(self):
        log_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(filename)s:%(lineno)d | %(message)s"
        )
        return logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")

    def _create_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self._create_log_formatter())
        return console_handler

    def _create_file_handler(self):
        file_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / f"{self.name}.log",
            maxBytes=self.max_bytes,
            backupCount=self.backup_count,
        )
        file_handler.setFormatter(self._create_log_formatter())
        return file_handler
