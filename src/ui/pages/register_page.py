from playwright.sync_api import Page
from ui.pages.base_page import BasePage
from utils.config import Config

class RegisterPage(BasePage):
    """注册页面"""

    def navigate(self):
        '''导航到注册页面'''
        self.page.goto(f"{Config.UI_URL}/register")
        self.wait_for_page_load()
        return self
    
    @property
    def page_title(self):
        '''注册页面标题'''
        return self.page.locator(".layout-content-container h2")
    
    @property
    def username_input(self):
        '''用户名输入框'''
        return self.page.locator("input[placeholder='请输入用户名']")
    
    @property
    def password_input(self):
        '''密码输入框'''
        return self.page.locator("input[placeholder='请输入密码']")
    
    @property
    def phone_input(self):
        '''手机号输入框'''
        return self.page.locator("input[placeholder='请输入手机号']")

    @property
    def submit_button(self):
        '''注册按钮'''
        return self.page.locator("button.cursor-pointer")

    @property
    def go_login_page_btn(self):
        '''登录页面按钮'''
        return self.page.locator("p.underline")
    
    @property
    def error_message(self):
        '''注册错误提示信息'''
        return self.page.locator(".el-message__content")
    
    def register(self, username: str, password: str, phone: str):
        '''注册'''
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.phone_input.fill(phone)
        self.submit_button.click()