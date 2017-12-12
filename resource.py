from .api import default_api


class Resource(object):
    def __init__(self, attributes={}, api=None):
        self.__dict__.update(attributes)
        self.__dict__['api'] = api or default_api()
        self.__dict__['attributes'] = attributes

    def headers(self):
        pass


class Find(Resource):
    @classmethod
    def find(cls, path,**parameters):
        url = path.format(**parameters)
        api = default_api()
        return cls(api.get(url), api=api)


class Post(Resource):
    def post(self, path, data=None, **parameters):
        url = path.format(**parameters)
        return self.api.post(url, data)

class Get(Resource):
    def get(self, path, data=None, **parameters):
        url = path.format(**parameters)
        return self.api.get(url, data)
