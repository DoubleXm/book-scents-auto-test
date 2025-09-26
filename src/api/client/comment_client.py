from utils.http_client import Request

class CommentClient:
    
    def __init__(self):
        self.client = Request()

    def get_comment_list(self, book_id, **kwargs):
        response = self.client.get(f'/api/v1/comments/{book_id}',**kwargs)
        return response

    def create_comment(self, book_id, data = {}, **kwargs):
        response = self.client.post(f'/api/v1/comments/{book_id}', json = data, **kwargs)
        return response
