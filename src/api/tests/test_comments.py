import allure
import pytest
from pathlib import Path
from api.data.create_data import create_book_comment_data
from utils.helper import formatter_parameterize_data

test_data_path = (
    Path(__file__).parent.parent.parent / "api/data/comment_failed_paramter.json"
)


@allure.parent_suite("书香接口测试")
@allure.sub_suite("图书接口测试")
class TestComments:

    @allure.title("测试评论图书")
    def test_comments_case_01(self, book_comment_create):
        response = book_comment_create["response"]

        assert response.status_code == 200
        assert response.json()["content"] == "testcomment"
        assert response.json()["rating"] == 3

    @allure.title("测试评论列表获取 -> 空列表")
    def test_comments_case_02(self, comment_client, book_create):
        book_id = book_create["response"].json()["id"]
        response = comment_client.get_comment_list(book_id)

        assert response.status_code == 200
        assert len(response.json()["list"]) == 0

    @allure.title("测试评论列表获取 -> 非空列表")
    def test_comments_case_03(self, comment_client, book_comment_create):
        book_id = book_comment_create["book_id"]
        response = comment_client.get_comment_list(book_id)

        assert response.status_code == 200
        assert len(response.json()["list"]) == 1
        assert response.json()["list"][0]["content"] == "testcomment"
        assert response.json()["list"][0]["rating"] == 3

    @pytest.mark.parametrize(
        "test_input, test_expect", formatter_parameterize_data(test_data_path)
    )
    @allure.title("测试创建评论边界值 -> {test_expect}")
    def test_comments_case_04(
        self, book_create, comment_client, test_input, test_expect
    ):
        token = book_create["token"]
        book_id = book_create["response"].json()["id"]

        response = comment_client.create_comment(
            book_id, test_input, headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == test_expect["status_code"]
        assert response.json()["message"] == test_expect["message"]

    @allure.title("测试创建评论 -> 书籍不存在")
    def test_comments_case_06(self, comment_client, user_register):
        token = user_register.json()["token"]
        book_id = 999999
        data = create_book_comment_data()
        response = comment_client.create_comment(
            book_id, data, headers={"Authorization": f"Bearer {token}"}
        )

        assert response.status_code == 404
        assert response.json()["message"] == "书籍不存在"

    @allure.title("测试创建评论 -> 没有携带 token")
    def test_comments_case_07(self, comment_client, book_create):
        book_id = book_create["response"].json()["id"]
        data = create_book_comment_data()
        response = comment_client.create_comment(book_id, data)

        assert response.status_code == 401
        assert response.json()["message"] == "缺少令牌"
