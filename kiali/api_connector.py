from __future__ import unicode_literals
import urllib3
import requests
import requests.utils
from requests.auth import HTTPBasicAuth


class KialiApiConnector():

    def __init__(self, hostname, port, scheme, verify, auth, max_retries, cookies=None):
        self.hostname = hostname
        self.port = port
        self.cookies = cookies
        self.scheme = scheme
        self.auth = auth
        self.verify = verify
        self.max_retries = max_retries

    def retrieve_url(self, path):
        return requests.utils.urlunparse((self.scheme, self.hostname, path, None, None, None))

    def create_session(self):
        session = requests.Session()
        session.auth = self.auth
        if self.cookies != None:
            session.cookies = self.cookies
        requests.adapters.HTTPAdapter(max_retries=self.max_retries)
        session.headers.update({'Content-Type': 'application/json'})
        return session

    # Factory Method of HTTP Request
    def dispatcher(self, url, params=None, http_method='GET', data=None):
        if http_method is 'GET':
            return self.get(url=url, params=params)

        if http_method is 'POST':
            return self.post(url=url, params=params, data=data)

        if http_method is 'PATCH':
            return self.patch(url=url, params=params, data=data)

        if http_method is 'DELETE':
            return self.delete(url=url, params=params, data=data)


    def get(self, url, params=None):
        session = self.create_session()
        return session.get(url=self.retrieve_url(url), verify=self.verify, params=params)

    def post(self, url, data, params=None):
        session = self.create_session()
        return session.post(url=self.retrieve_url(url), verify=self.verify, data=data, params=params)

    def patch(self, url, data, params=None):
        session = self.create_session()
        return session.patch(url=self.retrieve_url(url), verify=self.verify, data=data, params=params)

    def delete(self, url, data, params=None):
        session = self.create_session()
        return session.delete(url=self.retrieve_url(url), verify=self.verify, data=data, params=params)


class KialiHTTPSApiConnector(KialiApiConnector):
    """
    Creates new client for Kiali based on HTTPS
    """

    def __init__(self, hostname, port, scheme, username, password, verify, max_retries):

        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=HTTPBasicAuth(username, password), verify=verify, max_retries=max_retries)


class KialiNoAuthApiConnector(KialiApiConnector):
    """
        Creates new client for Kiali based on HTTP
        """

    def __init__(self, hostname, port, scheme, verify, max_retries):
        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=None, verify=verify, max_retries=max_retries)

class KialiOAuthApiConnector(KialiApiConnector):
    """
        Creates new client for Kiali based on OAuth
        """

    def __init__(self, hostname, port, scheme, verify, max_retries, swagger, token):
        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=None, verify=verify, max_retries=max_retries)

        oauth_url = self.retrieve_url(swagger.construct_url('Authenticate'))
        oauth_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        oauth_payload = "access_token=" + token + "&expires_in=86400"
        response = requests.request("POST", oauth_url, data=oauth_payload, headers=oauth_headers, verify=verify)
        self.cookies = response.cookies