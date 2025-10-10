from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_timeout(self, timeout: int = 5000):
        """等待指定超时时间"""
        self.page.wait_for_timeout(timeout)

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        """等待指定选择器出现"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def wait_for_page_load(self, timeout: int = 5000):
        """等待页面加载完成"""
        self.page.wait_for_load_state("networkidle", timeout=timeout)

    def take_screenshot(self, name: str):
        """截图"""
        self.page.screenshot(path=f"artifacts/screenshots/{name}.png")
