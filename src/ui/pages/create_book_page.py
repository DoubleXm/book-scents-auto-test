from ui.pages.base_page import BasePage
from utils.config import Config


class CreateBookPage(BasePage):
    
    def navigate(self):
        self.page.goto(f"{Config.UI_URL}/book/upload")
        self.wait_for_page_load()
        return self
    
    def create_book(self, book_name='', book_author='', book_desc='', book_cover=''):
        self.book_name_input.fill(book_name)
        self.book_author_input.fill(book_author)
        self.book_desc_input.fill(book_desc)
        # 参考：https://playwright.dev/python/docs/input#upload-files
        if book_cover:
            self.book_cover_input.set_input_files(book_cover)

        self.create_book_btn.click()
    
    @property
    def page_title(self):
        return self.page.locator('p.font-bold')
    
    @property
    def book_name_input(self):
        return self.page.locator('input[placeholder="请输入书籍名称"]')
    
    @property
    def book_author_input(self):
        return self.page.locator('input[placeholder="请输入作者"]')
    
    @property
    def book_desc_input(self):
        return self.page.locator('textarea[placeholder="请输入书籍描述"]')

    @property
    def book_cover_input(self):
        return self.page.locator('input[type="file"]')
    
    @property
    def create_book_btn(self):
        return self.page.locator('button.flex')
    
    @property
    def warning_message(self):
        return self.page.locator('.el-message.el-message--warning .el-message__content')
    
    @property
    def error_message(self):
        return self.page.locator('.el-message.el-message--error .el-message__content')