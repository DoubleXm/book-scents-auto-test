import allure
import pytest
from playwright.sync_api import expect
from pathlib import Path
import json

from utils.config import Config
from utils.helper import formatter_parameterize_data


test_data_path = Path(__file__).parent.parent.parent / 'ui/data/login_paramter.json'

@allure.parent_suite('书香 UI 测试')
@allure.sub_suite('登录页面测试')
class  TestLoginPage:

    @allure.title('测试登录失败 -> 用户名或密码错误')
    def test_login_page_01(self, login_page):
        login_page.navigate().login("111", "222")
        
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_have_text("用户名或密码错误")


    @allure.title('测试登录成功 -> 跳转首页')
    def test_login_page_02(self, login_page):
        login_page.navigate().login("张三", "password123")

        expect(login_page.page).to_have_url(f"{Config.UI_URL}/")


    @allure.title('测试登录 -> 跳转注册页面')
    def test_login_page_03(self, login_page, register_page):
        login_page.navigate().go_register_page_btn.click()

        expect(login_page.page).to_have_url(f"{Config.UI_URL}/register")
        expect(register_page.page_title).to_have_text("注册")


    @allure.title('测试登录 -> title 文案')
    def test_login_page_04(self, login_page):
        expect(login_page.navigate().page_title).to_have_text("登录到您的帐户")


    @allure.title('测试登录 -> 元素可见')
    def test_login_page_05(self, login_page):
        login = login_page.navigate()

        expect(login.username_input).to_be_visible()
        expect(login.password_input).to_be_visible()
        expect(login.submit_button).to_be_visible()
        expect(login.go_register_page_btn).to_be_visible()


    @pytest.mark.parametrize('test_input, test_expect', formatter_parameterize_data(test_data_path))
    @allure.title('测试登录异常边界 -> {test_input}')
    def test_login_page_06(self, login_page, test_input, test_expect):
        try:
            login_page.navigate().login(test_input["username"], test_input["password"])

            expect(login_page.error_message).to_be_visible()
            expect(login_page.error_message).to_have_text(test_expect["message"])
        except AssertionError as e:
            login_page.take_screenshot(f"test_login_page_06_{test_input['username']}_{test_input['password']}")
            raise e
        
        # 如果断言成功，则等待错误信息消失，以便下一条测试不受影响
        # 等待这次的错误信息消失，最多等待3秒
        login_page.error_message.wait_for(state="hidden", timeout=5000)


    @allure.title('测试登录成功 -> 跳转首页')
    def test_login_page_07(self, login_page):
        login_page.navigate().login("张三", "password123")

        # 等待用户信息加载到 localStorage 中
        login_page.wait_for_timeout(2000)
        user_local = login_page.page.evaluate("() => window.localStorage.getItem('user');")

        if isinstance(user_local, str):
            user = json.loads(user_local)
        else:
            user = user_local

        expect(login_page.page).to_have_url(f"{Config.UI_URL}/")
        # expect 只能用于判定 playwright 对象，普通的数据结构仍然要使用 assert 断言
        assert user['token'] is not None
        assert user['profile']['mobile'] == "13800138001"
        assert user['profile']['name'] == "张三"
