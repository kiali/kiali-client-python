from kiali.client import KialiBaseClient

class KialiClient(KialiBaseClient):

    def namespace_list(self):
        return self._get(self._get_namespace_url())

    def istio_config_list(self, namespace):
        return self._get(self._get_istio_config_url(namespace))

    def istio_config_detail(self, namespace, object_type, object_name):
        return self._get(self._get_istio_config_detail_url(namespace, object_type, object_name))

    def service_list(self, namespace):
        return self._get(self._get_service_list_url((namespace)))

    def service_detail(self, namespace, service):
        return self._get(self.get_service_detail_url(namespace, service))

    def service_metric(self, namespace, service):
        return self._get(self._get_service_metric_url(namespace, service))

    def service_health(self, namespace, service):
       return self._get(self._get_service_health_url(namespace, service))

    def service_validation(self, namespace, service):
        return self._get(self._get_service_validation_url(namespace, service))

    def graph_namespace(self, namespace, params={}):
        return self._get(self._get_graph_namespace_url(namespace), **params)

    def graph_service(self, namespace, service, params={}):
        return self._get(self._get_graph_service_url(namespace, service), **params)


