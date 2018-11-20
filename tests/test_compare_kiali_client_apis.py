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

    assert old_namespacelist.json() == new_namespace_list.json()


def test_istio_config_details():
    path = {'namespace': 'istio-system', 'object_type': 'rules', 'object': 'promtcp'}

    old_istio_config_details_url = "/api/namespaces/{0}/istio/{1}/{2}".format(path.get('namespace'), path.get('object_type'), path.get('object'))
    old_istio_config_details = kiali_client.request(plain_url=old_istio_config_details_url)
    assert old_istio_config_details is not None

    new_istio_config_details = kiali_client.request(methodname='istioConfigDetails', path=path)
    assert new_istio_config_details is not None

    assert old_istio_config_details.json() == new_istio_config_details.json()


def test_graph_namespace():
    VERSIONED_APP_PARAMS = {'namespace': 'bookinfo', 'graphType': 'versionedApp', 'duration': '60s'}
    WORKLOAD_PARAMS = {'namespace': 'bookinfo', 'graphType': 'workload', 'duration': '60s'}
    APP_PARAMS = {'namespace': 'bookinfo','graphType': 'app', 'duration': '60s'}

    old_graph_namespace = 'api/namespaces/graph'

    # This step is necessary because even though the JSON is supposed to be equals, since they are generated on
    # different timestamps, the timestamp element must be removed first
    new_versioned_app_params = conftest.remove_timestamp_from_json(kiali_client.request(methodname='graphNamespaces', query=VERSIONED_APP_PARAMS).json())
    old_versioned_app_params = conftest.remove_timestamp_from_json(kiali_client.request(plain_url=old_graph_namespace, query=VERSIONED_APP_PARAMS).json())
    assert old_versioned_app_params is not None
    assert new_versioned_app_params is not None

    assert old_versioned_app_params == new_versioned_app_params

    new_workload_params = conftest.remove_timestamp_from_json(
        kiali_client.request(methodname='graphNamespaces', query=WORKLOAD_PARAMS).json())
    old_workload_params = conftest.remove_timestamp_from_json(
        kiali_client.request(plain_url=old_graph_namespace, query=WORKLOAD_PARAMS).json())
    assert old_workload_params is not None
    assert new_workload_params is not None

    assert old_workload_params == new_workload_params

    new_app_params = conftest.remove_timestamp_from_json(
        kiali_client.request(methodname='graphNamespaces', query=APP_PARAMS).json())
    old_app_params = conftest.remove_timestamp_from_json(
        kiali_client.request(plain_url=old_graph_namespace, query=APP_PARAMS).json())
    assert old_app_params is not None
    assert new_app_params is not None

    assert old_app_params == new_app_params
