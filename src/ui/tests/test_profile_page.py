import allure
from playwright.sync_api import expect
from utils.config import Config

@allure.parent_suite('书香 UI 测试')
@allure.sub_suite('个人信息页面测试')
class TestProfilePage:

    @allure.title('测试用户信息显示')
    def test_profile_page_01(self, login, profile_page):
        login("张三", "password123")
        # 等待登录之后确保页面加载后再次跳转
        profile_page.wait_for_timeout(2000)
        profile_page.navigate()

        expect(profile_page.page_title).to_have_text("个人信息")
        expect(profile_page.user_cover).to_be_visible()
        # expect(profile_page.user_cover).to_have_attribute("style", "background-image: url(https://randomuser.me/api/portraits/men/76.jpg);")
        expect(profile_page.user_name_bold).to_have_text("张三")
        expect(profile_page.user_name_label).to_have_text("用户名: 张三")
        expect(profile_page.user_name_input).to_have_value("张三")
        expect(profile_page.phone_input).to_have_value("13800138001")
        expect(profile_page.logout_btn).to_be_visible()
        expect(profile_page.logout_btn).to_have_text("退出登录")
        

    @allure.title('退出登录')
    def test_profile_page_02(self, profile_page):
        profile_page.navigate().logout_btn.click()
        
        expect(profile_page.page).to_have_url(f"{Config.UI_URL}/login")
