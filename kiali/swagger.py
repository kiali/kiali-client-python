import re
import warnings
from urllib.parse import urlencode
import requests
from swagger_parser import SwaggerParser


class KialiSwaggerParser:

    def __init__(self, swagger_address, custom_base_path=None):
        json_object = requests.get(swagger_address).json()

        if custom_base_path is not None:
            json_object['basePath'] = custom_base_path + json_object['basePath']
            
        self.swagger = SwaggerParser(swagger_dict=json_object)


    def construct_url(self, operation, path=None, params=None):
        try:
            base_url = self.swagger.operation.get(operation)[0]
        except TypeError:
            raise Exception('Name not found on Swagger File')

        if path is not None:
            for key, value in path.items():
                base_url = re.sub("{" + key + "}", value, base_url)

        if params is not None:
            base_url = base_url + '?' + urlencode(params)

        return base_url

