import pytest
from utils.db_client import db_client
from utils.config import config
from utils.logger import test_logger

# Page 为了类型提示
from playwright.sync_api import sync_playwright, Page
from ui.pages.login_page import LoginPage
from ui.pages.register_page import RegisterPage
from ui.pages.profile_page import ProfilePage
from ui.pages.create_book_page import CreateBookPage


@pytest.fixture(scope="session")
def logger():
    """日志 fixture"""
    return test_logger


@pytest.fixture(scope="session")
def db_cursor():
    """数据库游标 fixture"""
    cursor = db_client()
    yield cursor
    cursor.close()


@pytest.fixture(scope="session")
def browser(logger):
    """浏览器 fixture"""
    logger.info(f"启动浏览器 {config.UI_BROWSER} 无头模式: {config.UI_HEADLESS}")
    with sync_playwright() as p:
        if config.UI_BROWSER == "chrome":
            browser = p.chromium.launch(headless=config.UI_HEADLESS)
        elif config.UI_BROWSER == "firefox":
            browser = p.firefox.launch(headless=config.UI_HEADLESS)
        elif config.UI_BROWSER == "webkit":
            browser = p.webkit.launch(headless=config.UI_HEADLESS)
        else:
            raise ValueError(f"不支持的浏览器类型: {config.UI_BROWSER}")

        yield browser
        browser.close()


# 默认的 page fixture, 作用域是 function, 这里选择重写
@pytest.fixture(scope="class")
def page(browser):
    """页面 fixture"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture(scope="class")
def login_page(page: Page, logger):
    """登录页面 fixture"""
    logger.info(f"打开登录页面 {config.UI_URL}/login")
    return LoginPage(page)


@pytest.fixture(scope="class")
def login(login_page: LoginPage, logger):
    """登录 fixture"""

    def _login(username: str, password: str):
        logger.info(f"登录用户 {username}")
        login_page.navigate().login(username, password)
        logger.info(f"用户 {username} 登录成功")

    return _login


@pytest.fixture(scope="class")
def register_page(page: Page, logger):
    """注册页面 fixture"""
    logger.info(f"打开注册页面 {config.UI_URL}/register")
    return RegisterPage(page)


@pytest.fixture(scope="class")
def profile_page(page: Page, logger):
    """用户中心页面 fixture"""
    logger.info(f"打开用户中心页面 {config.UI_URL}/profile")
    return ProfilePage(page)


@pytest.fixture(scope="class")
def create_book_page(page: Page, logger):
    """创建书籍页面 fixture"""
    logger.info(f"打开创建书籍页面 {config.UI_URL}/create_book")
    return CreateBookPage(page)
