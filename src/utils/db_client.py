from pymysql import connect, Connect
from utils.config import config


def db_client():
    try:
        conn = connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DATABASE,
        )
        cursor = conn.cursor()
        return cursor
    except Connect.Error as e:
        print(e)
        return None
