from ..resource import Get, Post
from ..api import configure as api_config
from ..config import __url_api__
import json


class Customer(Get, Post):
    path = '/partners/v1/customers'

    def find(self,**parameters):
        path_url= self.path + '{customerUrn}/orders/{orderUrn}'

        return self.get(path_url,**parameters)

    def create(self,data=None,**parameters):
        url= __url_api__+self.path
        data = data or self.attributes
        self.post(url,data,**parameters)



class CustomerList(Get, Post):
    path = '/partners/v1/users'

    def getList(self,**parameters):
        url = __url_api__+self.path
        response= self.get(url,**parameters)
        content = json.loads(response.content)


        customer =[]
        if not hasattr(content, u'error'):
            return map(lambda data:Customer(data),content)
        return customer

configure = api_config