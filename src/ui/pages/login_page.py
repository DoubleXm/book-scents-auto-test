from ui.pages.base_page import BasePage
from utils.config import config


class LoginPage(BasePage):
    """登录页面"""

    def navigate(self):
        """导航到登录页面"""
        self.page.goto(f"{config.UI_URL}/login")
        self.wait_for_page_load()
        return self

    @property
    def username_input(self):
        """用户名输入框"""
        return self.page.locator("input[placeholder='用户名']")

    @property
    def password_input(self):
        """密码输入框"""
        return self.page.locator("input[placeholder='密码']")

    @property
    def submit_button(self):
        """登录按钮"""
        return self.page.locator("button.cursor-pointer")

    @property
    def go_register_page_btn(self):
        """注册页面按钮"""
        return self.page.locator("p.underline")

    @property
    def error_message(self):
        """登录错误提示信息"""
        return self.page.locator(".el-message__content")

    @property
    def page_title(self):
        """登录页面标题"""
        return self.page.locator(".layout-content-container h2")

    def login(self, username: str, password: str):
        """登录"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        return self
