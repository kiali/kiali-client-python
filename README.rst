kiali-client-python
===================

This repository includes the necessary Python client libraries to access
Kiali remotely

Introduction
============

Python client to access Kiali (Service Mesh Observability), an
abstraction to invoke REST-methods on the server endpoint using urllib2.
No external dependencies, works with Python 2.7.x (tested on 2.7.14) and
Python 3.6.x (tested with Python 3.6.8, might work with newer versions
also).

License and copyright
---------------------

::

       Copyright 2018 Red Hat, Inc. and/or its affiliates
       and other contributors.

       Licensed under the Apache License, Version 2.0 (the "License");
       you may not use this file except in compliance with the License.
       You may obtain a copy of the License at

           http://www.apache.org/licenses/LICENSE-2.0

       Unless required by applicable law or agreed to in writing, software
       distributed under the License is distributed on an "AS IS" BASIS,
       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
       See the License for the specific language governing permissions and
       limitations under the License.

Installation
------------

To install, run ``python setup.py install`` if you installed from source
code, or ``pip install kiali-client`` if using pip.

General Usage
-------------

To instiante a Kiali Client, use KialiClient() method. It requires the a
host, username and password

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')

Another parameters possible to use with Client \* host (default:
``localhost``) \* scheme (default: ``http``, options: ``https`` and
``http``) \* port(default: ``80``)

Methods Available
~~~~~~~~~~~~~~~~~

Namespace List
^^^^^^^^^^^^^^

-  This method will return a list of ``Namespace`` object

-  No Required Parameters

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.namespace_list()
    [{'name': 'bookinfo'}, {'name': 'default'}, {'name': 'istio-system'}, {'name': 'kiali-test-box'}, {'name': 'kiali-test-breadth-sink'}, {'name': 'kiali-test-breath'}, {'name': 'kiali-test-circle'}, {'name': 'kiali-test-circle-callback'}, {'name': 'kiali-test-depth'}, {'name': 'kiali-test-depth-sink'}, {'name': 'kiali-test-hourglass'}, {'name': 'kube-public'}, {'name': 'kube-system'}, {'name': 'logging'}, {'name': 'management-infra'}, {'name': 'openshift'}, {'name': 'openshift-infra'}, {'name': 'openshift-node'}, {'name': 'samples'}]

Rules List
^^^^^^^^^^

-  This method will return a dictionary with ``Namespace`` object and a
   list of Istio ``Rules`` object

-  Required Parameter (``namespace``)

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.rules_list(namespace='istio-system')
    {'namespace': {'name': 'istio-system'}, 'rules': [{'name': 'kubeattrgenrulerule', 'actions': [{'handler': 'handler.kubernetesenv', 'instances': ['attributes.kubernetes']}]}, {'name': 'promhttp', 'match': 'context.protocol == "http"', 'actions': [{'handler': 'handler.prometheus', 'instances': ['requestcount.metric', 'requestduration.metric', 'requestsize.metric', 'responsesize.metric']}]}, {'name': 'promtcp', 'match': 'context.protocol == "tcp"', 'actions': [{'handler': 'handler.prometheus', 'instances': ['tcpbytesent.metric', 'tcpbytereceived.metric']}]}, {'name': 'stdio', 'match': 'true', 'actions': [{'handler': 'handler.stdio', 'instances': ['accesslog.logentry']}]}, {'name': 'tcpkubeattrgenrulerule', 'match': 'context.protocol == "tcp"', 'actions': [{'handler': 'handler.kubernetesenv', 'instances': ['attributes.kubernetes']}]}]}

Rule Detail
^^^^^^^^^^^

-  This method will return a ``Rule`` object with ``Namespace`` object
-  Required Parameter (``namespace``, ``rule``)

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.rule_details(namespace="istio-system", rule="promhttp")
    {'name': 'promhttp', 'match': 'context.protocol == "http"', 'actions': [{'handler': {'name': 'handler', 'adapter': 'prometheus', 'spec': {'metrics': [{'instance_name': 'requestcount.metric.istio-system', 'kind': 'COUNTER', 'label_names': ['source_service', 'source_version', 'destination_service', 'destination_version', 'response_code', 'connection_mtls'], 'name': 'request_count'}, {'buckets': {'explicit_buckets': {'bounds': [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]}}, 'instance_name': 'requestduration.metric.istio-system', 'kind': 'DISTRIBUTION', 'label_names': ['source_service', 'source_version', 'destination_service', 'destination_version', 'response_code', 'connection_mtls'], 'name': 'request_duration'}, {'buckets': {'exponentialBuckets': {'growthFactor': 10, 'numFiniteBuckets': 8, 'scale': 1}}, 'instance_name': 'requestsize.metric.istio-system', 'kind': 'DISTRIBUTION', 'label_names': ['source_service', 'source_version', 'destination_service', 'destination_version', 'response_code', 'connection_mtls'], 'name': 'request_size'}, {'buckets': {'exponentialBuckets': {'growthFactor': 10, 'numFiniteBuckets': 8, 'scale': 1}}, 'instance_name': 'responsesize.metric.istio-system', 'kind': 'DISTRIBUTION', 'label_names': ['source_service', 'source_version', 'destination_service', 'destination_version', 'response_code', 'connection_mtls'], 'name': 'response_size'}, {'instance_name': 'tcpbytesent.metric.istio-system', 'kind': 'COUNTER', 'label_names': ['source_service', 'source_version', 'destination_service', 'destination_version', 'connection_mtls'], 'name': 'tcp_bytes_sent'}, {'instance_name': 'tcpbytereceived.metric.istio-system', 'kind': 'COUNTER', 'label_names': ['source_service', 'source_version', 'destination_service', 'destination_version', 'connection_mtls'], 'name': 'tcp_bytes_received'}]}}, 'instances': [{'name': 'responsesize', 'template': 'metric', 'spec': {'dimensions': {'connection_mtls': 'connection.mtls | false', 'destination_service': 'destination.service | "unknown"', 'destination_version': 'destination.labels["version"] | "unknown"', 'response_code': 'response.code | 200', 'source_service': 'source.service | "unknown"', 'source_version': 'source.labels["version"] | "unknown"'}, 'monitored_resource_type': '"UNSPECIFIED"', 'value': 'response.size | 0'}}, {'name': 'requestcount', 'template': 'metric', 'spec': {'dimensions': {'connection_mtls': 'connection.mtls | false', 'destination_service': 'destination.service | "unknown"', 'destination_version': 'destination.labels["version"] | "unknown"', 'response_code': 'response.code | 200', 'source_service': 'source.service | "unknown"', 'source_version': 'source.labels["version"] | "unknown"'}, 'monitored_resource_type': '"UNSPECIFIED"', 'value': '1'}}, {'name': 'requestduration', 'template': 'metric', 'spec': {'dimensions': {'connection_mtls': 'connection.mtls | false', 'destination_service': 'destination.service | "unknown"', 'destination_version': 'destination.labels["version"] | "unknown"', 'response_code': 'response.code | 200', 'source_service': 'source.service | "unknown"', 'source_version': 'source.labels["version"] | "unknown"'}, 'monitored_resource_type': '"UNSPECIFIED"', 'value': 'response.duration | "0ms"'}}, {'name': 'requestsize', 'template': 'metric', 'spec': {'dimensions': {'connection_mtls': 'connection.mtls | false', 'destination_service': 'destination.service | "unknown"', 'destination_version': 'destination.labels["version"] | "unknown"', 'response_code': 'response.code | 200', 'source_service': 'source.service | "unknown"', 'source_version': 'source.labels["version"] | "unknown"'}, 'monitored_resource_type': '"UNSPECIFIED"', 'value': 'request.size | 0'}}]}], 'namespace': {'name': 'istio-system'}}

Services List
^^^^^^^^^^^^^

-  This method will return a dictionary with ``Namespace`` object and
   list of ``Service`` object

-  Required Parameter (``namespace``)

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.services_list(namespace="istio-system")
    {'namespace': {'name': 'istio-system'}, 'services': [{'name': 'grafana', 'replicas': 1, 'availableReplicas': 1, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'istio-ingress', 'replicas': 1, 'availableReplicas': 1, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'istio-mixer', 'replicas': 1, 'availableReplicas': 1, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'istio-pilot', 'replicas': 1, 'availableReplicas': 1, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'jaeger-agent', 'replicas': 0, 'availableReplicas': 0, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'jaeger-collector', 'replicas': 0, 'availableReplicas': 0, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'jaeger-query', 'replicas': 0, 'availableReplicas': 0, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'kiali', 'replicas': 1, 'availableReplicas': 1, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'prometheus', 'replicas': 1, 'availableReplicas': 1, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}, {'name': 'zipkin', 'replicas': 0, 'availableReplicas': 0, 'unavailableReplicas': 0, 'istioSidecar': False, 'requestCount': '0', 'requestErrorCount': '0', 'errorRate': '0'}]}

Service Details
^^^^^^^^^^^^^^^

-  This method will return a ``Service`` object

-  Required Parameter (``namespace``, ``service``)

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.service_details(namespace='istio-system', service="grafana")
    {'name': 'grafana', 'type': 'ClusterIP', 'ip': '172.22.213.86', 'ports': [{'name': 'http', 'protocol': 'TCP', 'port': 3000}], 'endpoints': [{'addresses': [{'kind': 'Pod', 'name': 'grafana-274859801-q5ggz', 'ip': '172.20.12.5'}], 'ports': [{'name': 'http', 'protocol': 'TCP', 'port': 3000}]}], 'dependencies': {}, 'deployments': [{'name': 'grafana', 'template_annotations': {'sidecar.istio.io/inject': 'false'}, 'labels': {'app': 'grafana'}, 'created_at': '2018-04-10T12:16:35Z', 'replicas': 1, 'available_replicas': 1, 'unavailable_replicas': 0, 'autoscaler': {'name': '', 'labels': None, 'created_at': '', 'min_replicas': 0, 'max_replicas': 0, 'target_cpu_utilization_percentage': 0, 'current_replicas': 0, 'desired_replicas': 0}}]}

Service Metrics
'''''''''''''''

-  This method will return a dictonary of Service metrics

-  Required Parameter (``namespace``, ``service``)

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.service_metrics(namespace='istio-system', service="grafana")
    {'metrics': {'request_count_in': {'matrix': []}, 'request_count_out': {'matrix': []}, 'request_error_count_in': {'matrix': []}, 'request_error_count_out': {'matrix': []}}, 'histograms': {'request_duration_in': {'average': {'matrix': []}, 'median': {'matrix': []}, 'percentile95': {'matrix': []}, 'percentile99': {'matrix': []}}, 'request_duration_out': {'average': {'matrix': []}, 'median': {'matrix': []}, 'percentile95': {'matrix': []}, 'percentile99': {'matrix': []}}, 'request_size_in': {'average': {'matrix': []}, 'median': {'matrix': []}, 'percentile95': {'matrix': []}, 'percentile99': {'matrix': []}}, 'request_size_out': {'average': {'matrix': []}, 'median': {'matrix': []}, 'percentile95': {'matrix': []}, 'percentile99': {'matrix': []}}, 'response_size_in': {'average': {'matrix': []}, 'median': {'matrix': []}, 'percentile95': {'matrix': []}, 'percentile99': {'matrix': []}}, 'response_size_out': {'average': {'matrix': []}, 'median': {'matrix': []}, 'percentile95': {'matrix': []}, 'percentile99': {'matrix': []}}}}
    metrics = client.service_metrics(namespace='istio-system', service="grafana")

Service Heath
'''''''''''''

-  This method will return a ``Health`` object

-  Required Parameter (``namespace``, ``service``)

Usage Example:

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.service_health(namespace='istio-system', service="grafana")
    {'healthyReplicas': 1, 'totalReplicas': 1}

Graph Namespace
'''''''''''''''

-  This method will return a ``Graph``, containing a dictionary with
   array of ``Node`` object and array of ``Edges``
-  Required Parameter (``namespace``)
-  Additional Parameters that can be included eg: {params={'interval':
   '7d', offset: '30m'}}

Usage example

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.graph_namespace(namespace='kiali-test-depth')
    {'elements': {'nodes': [{'data': {'id': 'n1', 'version': 'unknown', 'text': 'a <1.00pm>', 'rate': '1.0000', 'service': 'a.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n2', 'version': 'unknown', 'text': 'b', 'rate': '0.9983', 'service': 'b.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n3', 'version': 'unknown', 'text': 'c', 'rate': '0.9983', 'service': 'c.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n4', 'version': 'unknown', 'text': 'd', 'rate': '1.0000', 'service': 'd.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n5', 'version': 'unknown', 'text': 'e', 'rate': '1.0000', 'service': 'e.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n6', 'version': 'unknown', 'text': 'f', 'rate': '1.0000', 'service': 'f.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n0', 'version': 'unknown', 'text': 'unknown', 'service': 'unknown'}}], 'edges': [{'data': {'id': 'e0', 'source': 'n0', 'target': 'n1', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '1.0000'}}, {'data': {'id': 'e1', 'source': 'n1', 'target': 'n2', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '0.9983'}}, {'data': {'id': 'e2', 'source': 'n2', 'target': 'n3', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '0.9983'}}, {'data': {'id': 'e3', 'source': 'n3', 'target': 'n4', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '1.0000'}}, {'data': {'id': 'e4', 'source': 'n4', 'target': 'n5', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '1.0000'}}, {'data': {'id': 'e5', 'source': 'n5', 'target': 'n6', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '1.0000'}}]}}

Graph Service
'''''''''''''

-  This method will return a ``Graph``, containing a dictionary with
   array of ``Node`` object and array of ``Edges``
-  Required Parameter (``namespace``)
-  Additional Parameters that can be included eg: {params={'interval':
   '7d', offset: '30m'}}

Usage example

.. code:: python

    >>> from kiali import KialiClient
    >>> client = KialiClient(host='kiali-url.com', username='jdoe', password='password')
    >>> client.graph_service(namespace='kiali-test-depth', service='f')
    {'elements': {'nodes': [{'data': {'id': 'n0', 'version': 'unknown', 'text': 'e', 'service': 'e.kiali-test-depth.svc.cluster.local'}}, {'data': {'id': 'n1', 'version': 'unknown', 'text': 'f', 'rate': '1.0000', 'service': 'f.kiali-test-depth.svc.cluster.local'}}], 'edges': [{'data': {'id': 'e0', 'source': 'n0', 'target': 'n1', 'text': '1.00', 'color': 'green', 'style': 'solid', 'rate': '1.0000'}}]}}

