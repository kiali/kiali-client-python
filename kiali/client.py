"""
   Copyright 2015-2017 Red Hat, Inc. and/or its affiliates
   and other contributors.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE.txt-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from __future__ import unicode_literals

import codecs
import base64

try:
    import simplejson as json
except ImportError:
    import json



try:
    # Python 3
    from urllib.request import Request, urlopen, build_opener, install_opener, HTTPErrorProcessor
    from urllib.error import HTTPError, URLError
    from urllib.parse import quote, urlencode, quote_plus
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import Request, urlopen, URLError, HTTPError, HTTPErrorProcessor, build_opener, install_opener
    from urllib import quote, urlencode, quote_plus


class ApiObject(object):

    __slots__ = []

    defaults = dict()

    def __init__(self, dictionary=dict()):
        udict = ApiObject.transform_dict_to_underscore(dictionary)
        for k in self.__slots__:
            setattr(self, k, udict.get(k,self.defaults.get(k)))

    def to_json_object(self):
        dictionary = {}
        for attribute in self.__slots__:
            if hasattr(self,attribute):
                dictionary[attribute] = getattr(self,attribute)
        return ApiObject.transform_dict_to_camelcase(dictionary)

    @staticmethod
    def _to_camelcase(word):
        s = ''.join(x.capitalize() or '_' for x in word.split('_'))
        return ''.join([s[0].lower(), s[1:]])

    @staticmethod
    def _to_underscore(word):
        return ''.join(["_" + c.lower() if c.isupper() else c for c in word]).strip('_')

    @staticmethod
    def transform_dict_to_camelcase(dictionary):
        if dictionary is None:
            return dict()
        return dict((ApiObject._to_camelcase(k), v) for k, v in dictionary.items() if v is not None)

    @staticmethod
    def transform_dict_to_underscore(dictionary):
        if dictionary is None:
            return dict()
        return dict((ApiObject._to_underscore(k), v) for k, v in dictionary.items() if v is not None)

    @classmethod
    def list_to_object_list(cls, o):
        if o is not None:
            return [cls(ob) for ob in o]
        return []

class ApiJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ApiObject):
            return obj.to_json_object()
        else:
            return json.JSONEncoder.default(self, obj)

class KialiHTTPErrorProcessor(HTTPErrorProcessor):
    def http_response(self, request, response):
        return HTTPErrorProcessor.http_response(self, request, response)

    https_response = http_response



class KialiBaseClient(object):
    """
    Creates new client for Kiali
    """
    def __init__(self,
                 host='localhost',
                 port=80,
                 path='api',
                 scheme='http',
                 context=None,
                 username=None,
                 password=None):
        """
        A new instance of KialiClient is created with the following defaults:
        host = localhost
        port = 80
        """

        self.host = host
        self.port = port
        self.path = path
        self.context = context
        self.scheme = scheme
        self.username = username
        self.password = password

        self._setup_path()



    def _setup_path(self):
        opener = build_opener(KialiHTTPErrorProcessor())
        install_opener(opener)

        if self.path is None:
            class_name = self.__class__.__name__
            path_components = ''.join(["_" + c.lower() if c.isupper() else c for c in class_name]).split('_')
            path_components.pop()
            self.path = '/'.join(path_components)
        self.path = self.path.strip('/')

    def _get_base_url(self):
        return "{0}://{1}:{2}/{3}/".format(self.scheme, self.host, str(self.port), self.path)




    def _http(self, url, method, data=None, decoder=None, parse_json=True):
        res = None
        req = Request(url=url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Host', self.host)
        b64 = base64.b64encode((self.username + ':' + self.password).encode('utf-8'))
        req.add_header('Authorization', 'Basic {0}'.format(b64.decode()))


        if not isinstance(data, str):
            data = json.dumps(data, indent=2)

        reader = codecs.getreader('utf-8')

        if data:
            try:
                req.add_data(data)
            except AttributeError:
                req.data = data.encode('utf-8')
        try:
            req.get_method = lambda: method
            res = urlopen(req, context=self.context)

            if parse_json:
                if res.getcode() == 200:
                    data = json.load(reader(res), cls=decoder)
            else:
                data = reader(res).read()

            return data


        finally:
            if res:
                res.close()


    def _get(self, url, **url_params):
        params = urlencode(url_params)
        if len(params) > 0:
            url = '{0}?{1}'.format(url, params)

        return self._http(url, 'GET')

    def _service_url(self, path, params=None):
        url_array = [self._get_base_url()]

        str_path = path
        if isinstance(path,list):
            encoded_path = [quote_plus(p) for p in path]
            str_path  = '/'.join(encoded_path).strip('/')

        url_array.append(str_path)
        if params is not None:
            query = ''.join(['?', urlencode(params)])
            url_array.append(query)

        return ''.join(url_array)

    @staticmethod
    def _serialize_object(o):
        return json.dumps(o, cls=ApiJsonEncoder)


    def _get_url(self, parameter):
        return self._get_base_url() + parameter


    def status(self):
        return self._get(self._get_url('status'))

    def grafana(self):
        return self._get(self._get_url('grafana'))

    def jaeger(self):
        return self._get(self._get_url('jaeger'))

    def _get_namespaces_url(self):
        return self._get_base_url() + 'namespaces'

    def _get_rules_url(self, namespace):
        return self._get_namespaces_url() + "/" + namespace + '/rules'

    def _get_rules_detail_url(self, namespace, rule):
        return self._get_rules_url(namespace) + "/" + rule

    def _get_services_url(self, namespace):
        return self._get_namespaces_url() + "/" + namespace + "/services"

    def get_services_details_url(self, namespace, service):
        return self._get_services_url(namespace) + "/" + service

    def _get_service_metrics_url(self, namespace, service):
        return self.get_services_details_url(namespace, service) + "/metrics"

    def _get_service_health_url(self,namespace,service):
        return self.get_services_details_url(namespace, service) + "/health"

    def _get_graph_namespace_url(self, namespace):
        return self._get_namespaces_url() + "/" + namespace + "/graph"


    def _get_graph_service_url(self,namespace,service):
        return self.get_services_details_url(namespace, service) + "/graph"

