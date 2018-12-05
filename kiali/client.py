from kiali.api_connector import KialiHTTPSApiConnector
from kiali.api_connector import KialiNoAuthApiConnector
from kiali.swagger import KialiSwaggerParser

class KialiClient():
    def __init__(self, hostname='localhost', scheme='https', port='443', auth_type='https-user-password', username='admin', password='admin', verify=False, swagger_address='https://raw.githubusercontent.com/kiali/kiali/master/swagger.json', custom_base_path=None, max_retries=5):
        self.swagger_parser = KialiSwaggerParser(swagger_address=swagger_address, custom_base_path=custom_base_path)

        # TODO Add Oauth Connector
        if auth_type == 'https-user-password':
            self.api_connector = KialiHTTPSApiConnector(hostname=hostname, scheme=scheme, port=port, verify=verify, username=username, password=password, max_retries=max_retries)


        if auth_type == 'no-auth':
            self.api_connector = KialiNoAuthApiConnector(hostname=hostname, scheme=scheme, port=port, verify=verify)

    def request(self, method_name=None, path=None, params=None, plain_url=None):

        if plain_url is None:
            url = self.swagger_parser.construct_url(method_name, path, params)
            return self.api_connector.get(url)
        else:
            return self.api_connector.get(plain_url, params)

