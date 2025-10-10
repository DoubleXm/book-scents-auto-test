import pytest
from utils.db_client import db_client

# Page 为了类型提示
from playwright.sync_api import sync_playwright, Page
from ui.pages.login_page import LoginPage
from ui.pages.register_page import RegisterPage
from ui.pages.profile_page import ProfilePage
from ui.pages.create_book_page import CreateBookPage


@pytest.fixture(scope='session')
def db_cursor():
    """数据库游标 fixture"""
    cursor = db_client()
    yield cursor
    cursor.close()

@pytest.fixture(scope='session')
def browser():
    """浏览器 fixture"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# 默认的 page fixture, 作用域是 function, 这里选择重写
@pytest.fixture(scope='class')
def page(browser):
    """页面 fixture"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture(scope='class')
def login_page(page: Page):
    """登录页面 fixture"""
    return LoginPage(page)

@pytest.fixture(scope='class')
def login(login_page: LoginPage):
    """登录 fixture"""
    def _login(username: str, password: str):
        login_page.navigate().login(username, password)
    return _login


@pytest.fixture(scope='class')
def register_page(page: Page):
    """注册页面 fixture"""
    return RegisterPage(page)


@pytest.fixture(scope='class')
def profile_page(page: Page):
    """用户中心页面 fixture"""
    return ProfilePage(page)


@pytest.fixture(scope='class')
def create_book_page(page: Page):
    """创建书籍页面 fixture"""
    return CreateBookPage(page)
