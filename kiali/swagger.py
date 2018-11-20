import re
from urllib.parse import urlencode
import requests
from swagger_parser import SwaggerParser


class KialiSwaggerParser:

    def __init__(self, swagger_address='https://raw.githubusercontent.com/kiali/kiali/master/swagger.json'):
        json_object = requests.get(swagger_address).json()
        self.swagger = SwaggerParser(swagger_dict=json_object)


    def construct_url(self, operation, path=None, params=None):
        try:
            base_url = self.swagger.operation.get(operation)[0]
        except TypeError:
            raise Exception('Name not found on Swagger File')

        if path is not None:
            for key, value in path.items():
                base_url= re.sub("{" + key + "}", value, base_url)

        if params is not None:
            base_url = base_url + '?' + urlencode(params)

        return base_url

