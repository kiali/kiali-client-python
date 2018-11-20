import pytest
import yaml
from kiali.client import KialiClient

@pytest.fixture(scope='session')
def env_config(env_file):
    with open(env_file) as yamlfile:
        config = yaml.load(yamlfile)
    return config

@pytest.fixture(scope='session')
def get_kiali_https_auth_client():
    https_auth = env_config('env_basic_auth.yaml')
    return KialiClient(hostname=https_auth.get('kiali_hostname'), port=https_auth.get('kiali_port'), auth_type=https_auth.get(
        'kiali_auth_method'),
                       username=https_auth.get('kiali_username'), password=https_auth.get('kiali_password'), verify=https_auth.get(
            'kiali_verify_ssl_certificate'))


def remove_timestamp_from_json(json_element):
    del json_element['timestamp']
    return json_element