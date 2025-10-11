import allure
import pytest
from playwright.sync_api import expect

# 类型提示
from pymysql.cursors import Cursor
from pathlib import Path
from utils.helper import formatter_parameterize_data

test_cover_path = Path(__file__).parent.parent.parent / "assets/album-cover.jpeg"
test_create_book_data_path = (
    Path(__file__).parent.parent.parent / "ui/data/create_book_paramter.json"
)


@allure.parent_suite("书香 UI 测试")
@allure.sub_suite("创建书籍测试")
class TestCreateBook:

    @allure.title("测试创建书籍 -> 页面显示正常")
    def test_create_book_01(self, create_book_page):
        create_book_page.navigate()

        expect(create_book_page.page_title).to_have_text("上传书籍")
        expect(create_book_page.book_name_input).to_be_visible()
        expect(create_book_page.book_author_input).to_be_visible()
        expect(create_book_page.book_desc_input).to_be_visible()
        expect(create_book_page.book_cover_input).to_be_visible()
        expect(create_book_page.create_book_btn).to_be_visible()

    @allure.title("测试创建书籍 -> 没有 token")
    def test_create_book_02(self, create_book_page):
        create_book_page.navigate().create_book()

        expect(create_book_page.warning_message).to_have_text("请上传书籍封面")
        expect(create_book_page.error_message).to_have_text("缺少令牌")

    @allure.title("测试创建书籍 -> 成功创建书籍")
    def test_create_book_03(self, login, create_book_page, db_cursor: Cursor):
        login("张三", "password123")
        create_book_page.wait_for_timeout(1000)
        create_book_page.navigate().create_book(
            book_name="测试书籍",
            book_author="测试作者",
            book_desc="测试描述",
            book_cover=str(test_cover_path),
        )

        db_cursor.execute("SELECT * FROM books WHERE name = '测试书籍'")
        book = db_cursor.fetchone()

        assert book is not None
        assert book[1] == "测试书籍"
        assert book[2] == "测试作者"
        assert book[5] == "测试描述"
        assert book[6] is not None

        # 删除测试书籍
        db_cursor.execute(f"DELETE FROM books WHERE id = {book[0]}")
        db_cursor.connection.commit()

    @pytest.mark.parametrize(
        "test_input, test_expect",
        formatter_parameterize_data(test_create_book_data_path),
    )
    @allure.title("测试创建书籍 -> 异常边界 {test_input}")
    def test_create_book_04(self, create_book_page, test_input, test_expect, logger):
        logger.info(f"测试创建书籍 -> 异常边界 {test_input}")
        try:
            create_book_page.navigate().create_book(
                book_name=test_input["book_name"],
                book_author=test_input["book_author"],
                book_desc=test_input["book_desc"],
                book_cover=test_input["book_cover"],
            )

            logger.info(create_book_page.error_message.text_content())
            if "error_message" in test_expect:
                expect(create_book_page.error_message).to_be_visible()
                expect(create_book_page.error_message).to_have_text(
                    test_expect["error_message"]
                )
            if "warning_message" in test_expect:
                expect(create_book_page.warning_message).to_be_visible()
                expect(create_book_page.warning_message).to_have_text(
                    test_expect["warning_message"]
                )
        except AssertionError:
            logger.error("断言失败 -> %s, %s", test_input, test_expect)
            raise AssertionError("断言失败")

        create_book_page.error_message.wait_for(state="hidden", timeout=5000)
        create_book_page.warning_message.wait_for(state="hidden", timeout=5000)
