from kiali.client import KialiBaseClient

class KialiClient(KialiBaseClient):
    def namespace_list(self):
        return self._get(self._get_namespaces_url())

    def rules_list(self,namespace):
        return self._get(self._get_rules_url(namespace))


    def rule_details(self,namespace, rule):
        return self._get(self._get_rules_detail_url(namespace, rule))

    def services_list(self,namespace):
        return self._get(self._get_services_url((namespace)))


    def service_details(self, namespace, service):
        return self._get(self.get_services_details_url(namespace, service))

    def service_metrics(self,namespace,service):
        return self._get(self._get_service_metrics_url(namespace, service))

    def service_health(self,namespace,service):
       return self._get(self._get_service_health_url(namespace, service))


    def graph_namespace(self, namespace, params={}):
        return self._get(self._get_graph_namespace_url(namespace), **params)

    def graph_service(self, namespace, service, params={}):
        return self._get(self._get_graph_service_url(namespace, service), **params)


