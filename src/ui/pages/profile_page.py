from ui.pages.base_page import BasePage
from utils.config import Config

class ProfilePage(BasePage):
    
    def navigate(self):
        '''导航到用户中心页面'''
        self.page.goto(f"{Config.UI_URL}/profile")
        self.wait_for_page_load()
        return self

    @property
    def page_title(self):
        '''用户中心页面标题'''
        return self.page.locator("p.tracking-light")
    
    @property
    def user_cover(self):
        '''用户中心页面用户头像'''
        return self.page.locator("div.bg-center.w-32")
    
    @property
    def user_name_bold(self):
        '''用户中心页面用户名'''
        return self.page.locator(".flex-col > p.font-bold ")
    
    @property
    def user_name_label(self):
        '''用户中心页面用户名标签'''
        return self.page.locator(".flex-col > p.font-bold ~ p")
    
    @property
    def user_name_input(self):
        '''用户中心页面用户名输入框'''
        return self.page.locator(".layout-content-container :nth-child(3) input")
    
    @property
    def phone_input(self):
        '''用户中心页面手机号输入框'''
        return self.page.locator(".layout-content-container :nth-child(4) input")
    
    @property
    def logout_btn(self):
        '''用户中心页面退出登录按钮'''
        return self.page.locator(".layout-content-container :nth-child(5) button")