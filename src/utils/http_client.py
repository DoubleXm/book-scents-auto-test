import requests
from utils.config import config

class Request:

    def __init__(self, base_url=config.BASE_URL, timeout = config.API_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout

    # 将路径和 base_url 组装成完整 url
    def _build_url(self, url):
        return self.base_url + url
            
    def request(self, method, url, **kwargs):
        full_url = self._build_url(url)
        
        # 设置默认的超时时间
        if ('timeout' not in kwargs):
            kwargs['timeout'] = self.timeout
        try:
            r = requests.request(method, full_url, **kwargs)
            return r
        except Exception as e:
            return e
    
    def get(self, url, params = None, **kwargs):
        return self.request('GET', url, params=params, **kwargs)

    def post(self, url, data = None, json = None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)

    def put(self, url, data = None, json = None, **kwargs):
        return self.request('PUT', url, data=data, json=json, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)

    def patch(self, url, data = None, json = None, **kwargs):
        return self.request('PATCH', url, data=data, json=json, **kwargs)


if __name__ == '__main__':
    client = Request('http://127.0.0.1:5000')
    
    # get
    # r = client.get('/collect', params={ 'param1': 'value1' })
    # print(r.json())
    
    # post
    # r = client.post('/collect', json={ 'param1': 'value1' })
    # print(r.json())
    
    # upload file
    r = client.upload_file('/collect', 'test.txt', 'file')
    print(r.json())