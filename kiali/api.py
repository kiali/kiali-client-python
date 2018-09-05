from kiali.client import KialiBaseClient

class KialiClient(KialiBaseClient):

    # Namespace Related

    def namespace_list(self):
        return self._get(self._get_namespace_url())

    def namespace_metrics(self, namespace):
        return self._get(self._get_namespace_metrics_url(namespace))

    # Istio Related

    def istio_config_list(self, namespace):
        return self._get(self._get_istio_config_url(namespace))

    def istio_config_details(self, namespace, object_type, object_name):
        return self._get(self._get_istio_config_details_url(namespace, object_type, object_name))

    # Service Related

    def service_list(self, namespace):
        return self._get(self._get_service_list_url((namespace)))

    def service_details(self, namespace, service):
        return self._get(self.get_service_details_url(namespace, service))

    def service_metrics(self, namespace, service):
        return self._get(self._get_service_metrics_url(namespace, service))

    def service_health(self, namespace, service):
       return self._get(self._get_service_health_url(namespace, service))

    def service_validations(self, namespace, service):
        return self._get(self._get_service_validations_url(namespace, service))

    # Graph Related

    def graph_namespace(self, namespace, params={}):
        return self._get(self._get_graph_namespace_url(namespace), **params)

    def graph_service(self, namespace, service, params={}):
        return self._get(self._get_graph_service_url(namespace, service), **params)

    # Workload Related

    def workload_list(self, namespace):
        return self._get(self._get_workload_list_url((namespace)))

    def workload_details(self, namespace, workload):
        return self._get(self._get_workload_details_url(namespace, workload))

    # App Related

    def app_list(self, namespace):
        return self._get(self._get_app_list_url(namespace))

    def app_details(self, namespace, app):
        return self._get(self._get_app_details_url(namespace, app))
