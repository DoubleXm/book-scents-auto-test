from pathlib import Path

def create_user_data():
    data = {
        'username': 'testuser',
        'password': 'testpassword',
        'mobile': '13800138023'
    }
    return data

def create_book_data():
    data = {
        'name': 'testbook',
        'author': 'testauthor',
        'cover': open(Path(__file__).parent.parent.parent / 'assets/album-cover.jpeg', 'rb'),
        'description': 'testdescription',
        'url': 'https://www.baidu.com'
    }
    return data

def create_book_comment_data():
    data = {
        'rating': 3,
        'content': 'testcomment'
    }
    return data