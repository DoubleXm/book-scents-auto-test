import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Config:
    ENV: str = os.getenv('ENV')

    BASE_URL: str = os.getenv('API_GATEWAY')
    API_TIMEOUT: int = int(os.getenv('API_TIMEOUT', 3))

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    LOG_DIR = os.getenv('LOG_DIR', 'artifacts/logs')
    CONSOLE_OUTPUT = os.getenv('CONSOLE_OUTPUT', 'true').lower() == 'true'
    FILE_OUTPUT = os.getenv('FILE_OUTPUT', 'true').lower() == 'true'

    UI_HEADLESS = os.getenv('UI_HEADLESS', 'true').lower() == 'true'
    UI_BROWSER = os.getenv('UI_BROWSER', 'chrome')
    UI_URL = os.getenv('UI_URL')

    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'book_scents')

    @property
    def is_dev(self) -> bool:
        return self.ENV == 'dev'
    
    @property
    def is_test(self):
        return self.ENV == 'test'
    
    @property
    def is_prod(self):
        return self.ENV == 'prod'
    
config = Config()