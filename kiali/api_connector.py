from __future__ import unicode_literals

from abc import ABC

import urllib3
import requests
import requests.utils
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class KialiApiConnector(ABC):

    def __init__(self, hostname, port, scheme, verify, auth):
        self.hostname = hostname
        self.port = port
        self.scheme = scheme
        self.auth = auth
        self.verify = verify

    def retrieve_url(self, path):
        return requests.utils.urlunparse((self.scheme, (self.hostname + ":" +str(self.port)), path, None, None, None))

    def get(self, url, params=None):
        url = self.retrieve_url(url)
        session = requests.Session()
        session.auth = self.auth
        session.headers.update({'Host': self.hostname, 'Content-Type': 'application/json'})
        return session.get(url, verify=self.verify, params=params)


class KialiHTTPSApiConnector(KialiApiConnector):
    """
    Creates new client for Kiali based on HTTPS
    """

    def __init__(self, hostname, port, scheme, username, password, verify):
        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=HTTPBasicAuth(username, password), verify=verify)

