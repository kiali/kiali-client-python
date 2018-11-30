from __future__ import unicode_literals

from abc import ABC
import urllib3
import requests
import requests.utils
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class KialiApiConnector(ABC):

    def __init__(self, hostname, port, scheme, verify, auth, max_retry):
        self.hostname = hostname
        self.port = port
        self.scheme = scheme
        self.auth = auth
        self.verify = verify
        self.max_retry = max_retry

    def retrieve_url(self, path):
        return requests.utils.urlunparse((self.scheme, (self.hostname + ":" +str(self.port)), path, None, None, None))

    def get(self, url, params=None):
        url = self.retrieve_url(url)
        session = requests.Session()
        session.auth = self.auth
        requests.adapters.HTTPAdapter(max_retries=self.max_retry)
        session.headers.update({'Host': self.hostname, 'Content-Type': 'application/json'})
        return session.get(url, verify=self.verify, params=params)


class KialiHTTPSApiConnector(KialiApiConnector):
    """
    Creates new client for Kiali based on HTTPS
    """

    def __init__(self, hostname, port, scheme, username, password, verify, max_retry):

        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=HTTPBasicAuth(username, password), verify=verify, max_retry=max_retry)


class KialiNoAuthApiConnector(KialiApiConnector):
    """
        Creates new client for Kiali based on HTTPS
        """

    def __init__(self, hostname, port, scheme, verify):
        super().__init__(hostname=hostname, port=port, scheme=scheme,
                         auth=None, verify=verify)

