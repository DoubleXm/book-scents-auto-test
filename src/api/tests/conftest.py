import pytest
from utils.db_client import db_client
from api.client.user_client import UserClient
from api.client.book_client import BookClient
from api.client.comment_client import CommentClient
from api.data.create_data import create_user_data, create_book_data, create_book_comment_data


@pytest.fixture(scope='session')
def db_cursor():
    """数据库游标 fixture"""
    cursor = db_client()
    yield cursor
    cursor.close()

@pytest.fixture(scope='session')
def user_client():
    """用户客户端 fixture"""
    return UserClient()

@pytest.fixture(scope='session') 
def book_client():
    """图书客户端 fixture"""
    return BookClient()

@pytest.fixture(scope='session')
def comment_client():
    """评论客户端 fixture"""
    return CommentClient()


@pytest.fixture(scope='function')
def user_register(user_client, db_cursor):
    """注册用户"""
    data = create_user_data()
    response = user_client.user_register(json=data)
    yield response
    # 注册后删除用户
    if response.status_code == 200:
        db_cursor.execute("DELETE FROM users WHERE name = %s", (data['username'],))
        db_cursor.connection.commit()


@pytest.fixture(scope='function')
def book_create(book_client, db_cursor, user_register):
    """创建图书"""
    data = create_book_data()
    cover = data['cover']
    del data['cover']

    token = user_register.json()['token']
    response = book_client.create_book(data, files={ 'cover': cover }, headers={ 'Authorization': f'Bearer {token}' })
    yield {
        'response': response,
        'token': token
    }
    # 创建后删除图书
    if response.status_code == 200:
        book_id = response.json()['id']
        db_cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        db_cursor.connection.commit()

@pytest.fixture(scope='function')
def book_comment_create(book_create, comment_client, db_cursor):
    """创建图书评论"""
    token = book_create['token']
    book_id = book_create['response'].json()['id']

    data = create_book_comment_data()
    response = comment_client.create_comment(book_id, data, headers={ 'Authorization': f'Bearer {token}' })
    yield {
        'response': response,
        'token': token,
        'book_id': book_id
    }
    # 创建后删除评论
    if response.status_code == 200:
        comment_id = response.json()['id']
        db_cursor.execute("DELETE FROM comments WHERE id = %s", (comment_id,))
        db_cursor.connection.commit()
