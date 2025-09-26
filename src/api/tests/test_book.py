import allure
import pytest
from pathlib import Path
from utils.helper import formatter_parameterize_data

test_data_path = Path(__file__).parent.parent.parent / 'api/data/book_failed_paramter.json'
test_cover_path = Path(__file__).parent.parent.parent / 'assets/album-cover.jpeg'

@allure.parent_suite('书香接口测试')
@allure.sub_suite('图书接口测试')
class TestBook:

    @allure.title('测试创建图书')
    def test_book_case_01(self, book_create):
        assert book_create['response'].status_code == 200
        assert book_create['response'].json()['message'] == '上传成功'
    
    @pytest.mark.parametrize('test_input, test_expect', formatter_parameterize_data(test_data_path))
    @allure.title('测试创建图书失败 -> {test_expect}')
    def test_book_case_02(self, book_client, user_register, test_input, test_expect):
        token = user_register.json()['token']
        response = book_client.create_book(
            data=test_input, 
            files={ 'cover': open(test_cover_path, 'rb') },
            headers={ 'Authorization': f'Bearer {token}' }
        )
        assert response.status_code == test_expect['status_code']
        assert response.json()['message'] == test_expect['message']

    @allure.title('测试创建图书失败 -> 没有携带 token ')
    def test_book_case_03(self, book_client):
        response = book_client.create_book(
            data={
                'name': 'testbook',
                'author': 'testauthor',
                'description': 'testdescription',
                'url': 'https://www.baidu.com'
            },
            files={ 'cover': open(Path(__file__).parent.parent.parent / 'assets/album-cover.jpeg', 'rb') }, 
        )
        assert response.status_code == 401

    @allure.title('测试获取图书列表')
    def test_book_case_04(self, book_create, book_client):
        response = book_client.get_book_list({
            'pageSize': 10,
            'pageNum': 1,
            'name': ''
        })
        books = response.json()['list']
        create_book_id = book_create['response'].json()['id']
        
        assert response.status_code == 200
        assert create_book_id in [book['id'] for book in books]

        if len(books) > 0:
            first_book = books[0]
            assert first_book['name'] == 'testbook'
            assert first_book['author'] == 'testauthor'

    @allure.title('测试获取图书详情')
    def test_book_case_05(self, book_create, book_client):
        response = book_client.get_book_detail(book_create['response'].json()['id'])
        assert response.status_code == 200
        assert response.json()['name'] == 'testbook'
        assert response.json()['author'] == 'testauthor'

    @allure.title('测试图书阅读次数')
    def test_book_case_06(self, db_cursor, book_create, book_client):
        # 获取图书ID和token
        book_id = book_create['response'].json()['id']
        token = book_create['token']

        # 调用阅读记录接口
        response = book_client.book_read_record(book_id, headers={ 'Authorization': f'Bearer {token}' })
        assert response.status_code == 200

        # 确保数据库连接提交，以看到最新数据
        db_cursor.connection.commit()

        db_cursor.execute("SELECT hot FROM books WHERE id = %s", (book_id,))
        hot = db_cursor.fetchone()[0]
        assert hot == 1
        

