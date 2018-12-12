from __future__ import unicode_literals

from abc import ABC
import urllib3
import requests
import requests.utils
from requests.auth import HTTPBasicAuth


class KialiApiConnector(ABC):

    def __init__(self, hostname, port, scheme, verify, auth, max_retries):
        self.hostname = hostname
        self.port = port
        self.scheme = scheme
        self.auth = auth
        self.verify = verify
        self.max_retries = max_retries

    def retrieve_url(self, path):
        return requests.utils.urlunparse((self.scheme, (self.hostname + ":" +str(self.port)), path, None, None, None))

    def create_session(self):
        session = requests.Session()
        session.auth = self.auth
        requests.adapters.HTTPAdapter(max_retries=self.max_retries)
        session.headers.update({'Host': self.hostname, 'Content-Type': 'application/json'})
        return session

    # Factory Method of HTTP Request
    def dispatcher(self, url, params=None, http_method='GET', data=None):
        if http_method is 'GET':
            return self.get(url=url, params=params)

        if http_method is 'PATCH':
            return self.patch(url=url, params=params, data=data)


    def get(self, url, params=None):
        session = self.create_session()
        return session.get(url=self.retrieve_url(url), verify=self.verify, params=params)

    def patch(self, url, data, params=None):
        session = self.create_session()
        return session.patch(url=self.retrieve_url(url), data=data, params=params)


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

    def __init__(self, hostname, port, scheme, verify):
        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=None, verify=verify)

