import yaml
from pkg_resources import resource_string

from kiali.client import KialiClient

def env_config(env_file):
    yamlfile = resource_string(__name__, env_file)
    config = yaml.load(yamlfile)
    return config

def get_kiali_https_auth_client():
    https_auth = env_config('env_basic_auth.yaml')
    return KialiClient(hostname=https_auth.get('kiali_hostname'), port=https_auth.get('kiali_port'), auth_type=https_auth.get(
        'kiali_auth_method'),
                       username=https_auth.get('kiali_username'), password=https_auth.get('kiali_password'), verify=https_auth.get(
            'kiali_verify_ssl_certificate'), swagger_address=https_auth.get('kiali_swagger_address'), custom_base_path=https_auth.get('kiali_custom_base_context'))



def remove_timestamp_from_json(json_element):
    del json_element['timestamp']
    return json_element