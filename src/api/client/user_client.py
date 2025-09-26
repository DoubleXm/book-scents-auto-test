from utils.http_client import Request

class UserClient:
    
    def __init__(self):
        self.client = Request()

    def user_login(self, json = {}, **kwargs):
        response = self.client.post('/api/v1/login', json=json, **kwargs)
        return response
    
    def user_register(self, json = {}, **kwargs):
        response = self.client.post('/api/v1/register', json=json, **kwargs)
        return response