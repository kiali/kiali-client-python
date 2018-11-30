# Introduction
This repository includes the necessary Python client libraries to access Kiali remotely

## Installation

To install, run ``python setup.py install`` if you installed from source code, or ``pip install kiali-client`` if using pip.


## Create Client Connections
To start a Kiali Client, use KialiClient() method. It requires the `host`, `username` and `password` parameters

```python
>>> from kiali import KialiClient
>>> client = KialiClient(host='kiali-url.com')
```

Another parameters possible to use with Client
* host (default: `localhost`)
* scheme (default: `http`, options: `https` and `http`
* port (default: `443`)
* auth_type (default: `https-user-password`, options: `no-auth`; oauth will be added)
* username (default: `admin`)
* password (default: `admin`)
* verify   (default: `False`) - used for verify SSL certificates
* swagger_address (default: https://raw.githubusercontent.com/kiali/kiali/master/swagger.json') - address to swagger file


## Creating a Request on Kiali CLient

## Testing

```shell
$ git clone https://github.com/kiali/kiali-python-client.git

# Install Pip env
pip3 install pipenv

# Install Pipenv modules required
$ pipenv install

# Enable Virtualenv
$ pipenv shell

# Update config/env.yaml with kiali hostname and credentials

$ pytest -s tests/
```