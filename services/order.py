from ..resource import Get, Post, Find
from ..api import configure as api_config
from ..config import __url_api__
import json
class Order(Get, Post,Find):
    path = '/partners/v1/customers/'

    def find(self,**parameters):
        path_url= self.path + '{customer_urn}/orders/{orderUrn}'

        return self.find(path_url,**parameters)

    def create(self,data,**parameters):
        url = __url_api__ + self.path+'{customer_urn}/orders'
        data = data or self.attributes


        self.post(url,self.attributes,**parameters)



class OrderList(Get):
    path = '/partners/v1/customers'
    def getList(self, **parameters):
        url = __url_api__ + self.path+'/{customer_urn}/orders'
        response = self.get(url, **parameters)
        content = json.loads(response.content)

        order = []
        if not hasattr(content, u'error'):
            return map(lambda data: Order(data), content)
        return order

configure = api_config
