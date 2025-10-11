import os
import sys
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Config:
    def __init__(self):
        self.setup_config()

        self.ENV = os.getenv("ENV")
        self.BASE_URL = os.getenv("API_GATEWAY")
        self.API_TIMEOUT = int(os.getenv("API_TIMEOUT", 3))

        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
        self.LOG_DIR = os.getenv("LOG_DIR", "artifacts/logs")
        self.CONSOLE_OUTPUT = os.getenv("CONSOLE_OUTPUT", "true").lower() == "true"
        self.FILE_OUTPUT = os.getenv("FILE_OUTPUT", "true").lower() == "true"

        self.UI_HEADLESS = os.getenv("UI_HEADLESS").lower() == "true"
        self.UI_BROWSER = os.getenv("UI_BROWSER", "chrome")
        self.UI_URL = os.getenv("UI_URL")

        self.MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
        self.MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
        self.MYSQL_USER = os.getenv("MYSQL_USER", "root")
        self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
        self.MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "book_scents")

    def setup_config(self):
        file_name = None
        for i in sys.argv:
            if i.startswith("--env="):
                file_name = i.replace("--env=", "")
                break

        load_dotenv(
            # override=True,
            dotenv_path=(f".env.{file_name}" if file_name else ".env"),
        )

    @property
    def is_dev(self) -> bool:
        return self.ENV == "dev"

    @property
    def is_test(self):
        return self.ENV == "test"

    @property
    def is_prod(self):
        return self.ENV == "production"


config = Config()
