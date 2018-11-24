import re
import warnings
from urllib.parse import urlencode
import requests
from swagger_parser import SwaggerParser


class KialiSwaggerParser:

    def __init__(self, swagger_address):
        json_object = requests.get(swagger_address).json()
        self.swagger = SwaggerParser(swagger_dict=json_object)


    def construct_url(self, operation, path=None, params=None):
        try:
            base_url = self.swagger.operation.get(operation)[0]
        except TypeError:
            raise Exception('Name not found on Swagger File')

        if path is not None:
            for key, value in path.items():
                base_url = re.sub("{" + key + "}", value, base_url)

        # FIXME This code is a workaround for https://issues.jboss.org/projects/KIALI/issues/KIALI-1969
        if "api/api" in base_url:
            warnings.warn('The Method {0} contains a double /api on the swagger file. '
                          'Check https://issues.jboss.org/projects/KIALI/issues/KIALI-1969'.format(operation),
                          SyntaxWarning)
            base_url = re.sub('api/api', 'api', base_url)

        # FIXME This code is workaround for https://issues.jboss.org/projects/KIALI/issues/KIALI-1994
        if operation == 'Root':
            warnings.warn(
                'The Method {0} on the swagger file is directing to a non-existent path: {1}. Check https://issues.jboss.org/projects/KIALI/issues/KIALI-1994  '.format(operation,
                                                                                                      base_url),
                SyntaxWarning)
            base_url = re.sub('/api/', '/api', base_url)

        if params is not None:
            base_url = base_url + '?' + urlencode(params)

        return base_url

