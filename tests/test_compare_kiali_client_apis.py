import pytest
import tests.conftest as conftest

@pytest.fixture(scope="session", autouse=True)
def before_all_tests():
    global kiali_client
    kiali_client = conftest.get_kiali_https_auth_client()



def test_namespace_list():
    old_namespacelist_url = '/api/namespaces'
    old_namespacelist = kiali_client.request(plain_url=old_namespacelist_url)
    assert old_namespacelist is not None

    new_namespace_list = kiali_client.request(methodname='namespaceList')
    assert new_namespace_list is not None

    assert old_namespacelist.url == new_namespace_list.url
    assert old_namespacelist.json() == new_namespace_list.json()


def test_istio_config_details():
    path = {'namespace': 'istio-system', 'object_type': 'rules', 'object': 'promtcp'}

    old_istio_config_details_url = "/api/namespaces/{0}/istio/{1}/{2}".format(path.get('namespace'), path.get('object_type'), path.get('object'))

    old_istio_config_details = kiali_client.request(plain_url=old_istio_config_details_url)
    assert old_istio_config_details is not None

    new_istio_config_details = kiali_client.request(methodname='istioConfigDetails', path=path)
    assert new_istio_config_details is not None

    assert old_istio_config_details.url == new_istio_config_details.url

    assert old_istio_config_details.json() == new_istio_config_details.json()


def test_graph_namespace():
    VERSIONED_APP_PARAMS = {'namespace': 'bookinfo', 'graphType': 'versionedApp', 'duration': '60s'}
    WORKLOAD_PARAMS = {'namespace': 'bookinfo', 'graphType': 'workload', 'duration': '60s'}
    APP_PARAMS = {'namespace': 'bookinfo','graphType': 'app', 'duration': '60s'}

    request_list = [VERSIONED_APP_PARAMS, WORKLOAD_PARAMS, APP_PARAMS]

    old_graph_namespace_url = 'api/namespaces/graph'

    for graph_type in request_list:
        new_graph_type_request = kiali_client.request(methodname='graphNamespaces', query=graph_type)
        old_graph_type_request = kiali_client.request(plain_url=old_graph_namespace_url, query=graph_type)

        assert new_graph_type_request is not None and old_graph_type_request is not None
        assert new_graph_type_request.url == old_graph_type_request.url

        # This step is necessary because even though the JSON are supposed to be equals, since they are generated on
        # different timestamps, the timestamp element must be removed first
        new_graph_type_json = conftest.remove_timestamp_from_json(new_graph_type_request.json())
        old_graph_type_json = conftest.remove_timestamp_from_json(old_graph_type_request.json())

        assert new_graph_type_json == old_graph_type_json


