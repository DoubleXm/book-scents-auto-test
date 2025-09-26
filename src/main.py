from api.client.user_client import UserClient
from api.data.create_data import create_user_data, create_book_data
from api.client.book_client import BookClient
import requests
import pathlib
from utils.http_client import Request
from utils.db_client import db_client

if __name__ == '__main__':
    # user_client = UserClient()
    # book_client = BookClient()
    # # response = user_client.user_register(json=create_user_data())
    # headers = {
    #     'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTg4NzU3MzIsImlhdCI6MTc1ODc4OTMzMiwic3ViIjoiMjZhZTAxOGYtMDgzNy00MmNkLWJiNjgtOTI5ZGY0OTc4ZjhiIn0.SsATUqGwqOU6KRV6HJ_sLX7YzKytssk67JM9QWAbgk4',
    # }
    # # book_response = book_client.create_book(data=create_book_data(), json={}, headers=headers)
    # name, author, cover, description, url = create_book_data()
    # data = {
    #     'name': name,
    #     'author': author,
    #     'description': description,
    #     'url': url
    # }
    # # print(pathlib.Path(__file__).parent.parent / 'src/assets/album-cover.jpeg')
    # # book_response = book_client.create_book(
    # book_response = Request().post('/api/v1/books',
    # # book_response = requests.post(
    # # book_response = requests.request(
    # #     'POST',
    # #     'http://127.0.0.1:5001/api/v1/books',
    #     data=data,
    #     files={ 'cover': open(pathlib.Path(__file__).parent.parent / 'src/assets/album-cover.jpeg', 'rb')}, 
    #     headers=headers
    # )
    # print(book_response)

    cursor = db_client()

    cursor.execute('SELECT * FROM users WHERE name="testuser"')
    print(cursor.fetchall())