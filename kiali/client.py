from kiali.api_connector import KialiHTTPSApiConnector
from kiali.swagger import KialiSwaggerParser

class KialiClient():
    def __init__(self, hostname='localhost', scheme='https', port='443', auth_type='https', username='admin', password='admin', verify=False, swagger_address='https://raw.githubusercontent.com/kiali/kiali/master/swagger.json'):
        self.swagger_parser = KialiSwaggerParser(swagger_address)

        # TODO create other types of Auth
        if auth_type == 'https':
            self.api_connector = KialiHTTPSApiConnector(hostname=hostname, scheme=scheme, port=port, verify=verify, username=username, password=password)

    def request(self, method_name=None, path=None, params=None, plain_url=None):

        if plain_url is None:
            url = self.swagger_parser.construct_url(method_name, path, params)
            return self.api_connector.get(url)
        else:
            return self.api_connector.get(plain_url, params)

