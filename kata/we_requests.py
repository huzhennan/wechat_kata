# coding=utf-8
import requests
from requests import status_codes

class WeRequests(object):
    BASE_URL = 'https://open.weixin.qq.com/connect/oauth2/'

    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret

    def auth(self, redirect_uri, scope='snsapi_base', state=None):
        url = WeRequests.BASE_URL + "authorize"
        params = {
            'appid': self.app_id,
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            'scope': scope
        }

        if state:
            params['state'] = state

        r = requests.get(url, params=params)
        if r.status_code == status_codes.ok:
            return r.json()

    def get_access_token(self, code):
        url = WeRequests.BASE_URL + "access_token"
        params = {
            'appid': self.app_id,
            'secret': self.app_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }

        r = requests.get(url, params=params)
        return r.json()



    def get_snsapi_userinfo(self):
        pass


if __name__ == '__main__':
    we = WeRequests(app_id="my_app_id", app_secret="my_app_secret")
    print we.auth("http://www.baidu.com")

class WeRequests3rd(object):
    def __init__(self):
        pass
