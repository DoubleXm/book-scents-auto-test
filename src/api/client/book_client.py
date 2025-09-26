from utils.http_client import Request

class BookClient:
    
    def __init__(self):
        self.client = Request()

    def get_book_list(self, params = {}, **kwargs):
        response = self.client.get('/api/v1/books', params = params, **kwargs)
        return response
    
    def get_book_detail(self, book_id, **kwargs):
        response = self.client.get(f'/api/v1/books/{book_id}', **kwargs)
        return response
    
    def create_book(self, data={}, **kwargs):
        response = self.client.post('/api/v1/books', data=data, **kwargs)
        return response
    
    def book_read_record(self, book_id, **kwargs):
        response = self.client.patch(f'/api/v1/books/{book_id}/read', **kwargs)
        return response
