from kiali.models import *
from kiali.client import KialiBaseClient

class KialiClient(KialiBaseClient):
    def namespace_list(self):
        namespaces = self._get(self._get_namespaces_url())
        return Namespace.list_to_object_list(namespaces)

    def rules_list(self,namespace):
        dict = self._get(self._get_rules_url(namespace))
        dict["rules"] = Rule.list_to_object_list(dict["rules"])
        return dict


    def rule_details(self,namespace, rule):
        dict = self._get(self._get_rules_detail_url(namespace, rule))
        return Rule.list_to_object_list([dict])[0]

    def services_list(self,namespace):
        dict = self._get(self._get_services_url((namespace)))
        dict["services"] = Rule.list_to_object_list(dict["services"])
        return dict


    def service_details(self, namespace, service):
        dict = self._get(self.get_services_details_url(namespace, service))
        return Rule.list_to_object_list([dict])[0]

    def service_metrics(self,namespace,service):
        return self._get(self._get_service_metrics_url(namespace, service))

    def service_health(self,namespace,service):
       dict = self._get(self._get_service_health_url(namespace, service))
       return Health.list_to_object_list([dict])[0]


    def graph_namespace(self, namespace, params={}):
        dict = self._get(self._get_graph_namespace_url(namespace), **params)
        dict = Graph(dict)

        for node in dict.elements["nodes"]:
         node["data"] = Data(node["data"])
        for edge in dict.elements["edges"]:
         edge["data"] = Data(edge["data"])

        dict.elements["nodes"] = Node.list_to_object_list(dict.elements["nodes"])
        dict.elements["edges"] = Edge.list_to_object_list(dict.elements["edges"])

        return dict

    def graph_service(self, namespace, service, params={}):
        dict = self._get(self._get_graph_service_url(namespace, service), **params)
        dict = Graph(dict)

        for node in dict.elements["nodes"]:
            node["data"] = Data(node["data"])
        for edge in dict.elements["edges"]:
            edge["data"] = Data(edge["data"])

        dict.elements["nodes"] = Node.list_to_object_list(dict.elements["nodes"])
        dict.elements["edges"] = Edge.list_to_object_list(dict.elements["edges"])

        return dict

