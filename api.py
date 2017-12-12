import os
from . import exceptions
import requests
import json
from .config import __url_api__


class Api(object):
    def __init__(self, **kwargs):
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.token_access = None
        self.get_access_token()

    def get_access_token(self):
        # url = 'http://stageapi.glovoapp.com/partners/v1/oauth/token'
        url = __url_api__ + '/partners/v1/oauth/token'
        data = {
            "clientId": self.client_id,
            "clientSecret": self.client_secret,
            'grantType': 'password'
        }
        response = requests.post(url, json.dumps(data),
                                 headers={"content-type": "application/json", "accept": "application/json"})
        # response.content
        content = json.loads(response.content)

        if not hasattr(content, 'error'):
            self.token_access = content['token']

    def headers(self):
        header = {"content-type": "application/json", "accept": "application/json", "Authorization": self.token_access}
        return header

    def get(self, url, data):
        data = json.dumps(data) if data else None
        return requests.get(url, data,
                             headers=self.headers())

    def post(self, url, data):
        data = json.dumps(data) if data else None
        response = requests.post(url, data,
                                 headers=self.headers())
        return response


__API__ = None


def default_api():
    global __API__

    if __API__ is None:
        try:
            client_id = os.environ["GLOVO_CLIENT_ID"]
            client_secret = os.environ["GLOVO_CLIENT_SECRET"]

        except KeyError:
            raise exceptions.FailedConfig("Required GLOVO_CLIENT_ID and GLOVO_CLIENT_SECRET")

        __API__ = Api(client_id=client_id, client_secret=client_secret)

    return __API__


def configure(**config):
    global __API__
    __API__ = Api(**config)
    return __API__
