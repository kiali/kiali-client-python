# Introduction
This repository includes the necessary Python client libraries to access Kiali remotely

## Installation

To install, run ``python setup.py install`` if you installed from source code, or ``pip install kiali-client`` if using pip.


## General Usage
To instiante a Kiali Client, use KialiClient() method. It requires the `host`, `username` and `password` parameters

```python
>>> from kiali import KialiClient
>>> client = KialiClient(host='kiali-url.com')
```

Another parameters possible to use with Client
* host (default: `localhost`)
* scheme (default: `http`, options: `https` and `http`)
* port(default: `80`)
* username(default:`admin`)
* password(default:`admin`)


# Testing

```shell
$ git clone https://github.com/kiali/kiali-python-client.git



# Update config/env.yaml with kiali hostname and credentials

$ pytest -s tests/
```