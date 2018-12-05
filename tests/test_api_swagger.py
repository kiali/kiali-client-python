import pytest
import tests.conftest as conftest

@pytest.fixture(scope="session", autouse=True)
def before_all_tests():
    global kiali_client
    kiali_client = conftest.get_kiali_https_auth_client()



def test_swagger_double_api():
    swagger = kiali_client.swagger_parser.swagger

    for key, value in swagger.operation.items():
        assert not 'api/api' in value[0]

