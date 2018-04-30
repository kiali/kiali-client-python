from kiali.client import ApiObject

class Data (ApiObject):
    __slots__ = [
        'id', "source", 'target', 'version', 'text', 'color', 'style', 'rate', 'service', 'group_by',
        "is_root", "has_c_b", "parent"
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Health (ApiObject):
    __slots__ = [
        'healthy_replicas', 'total_replicas'
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Namespace(ApiObject):
    __slots__ = [
        'name'
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Node (ApiObject):
    __slots__ = [
        'data'
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Rule(ApiObject):
    __slots__ = [
        'name', 'match', 'actions', 'instances', 'namespace'
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Service (ApiObject):
    __slots__ = [
        'name', 'replicas', 'available_replicas', 'unavailable_replicas', 'istio_sidecar', 'request_count', 'request_error_count', 'error_rate',
        "labels", "type", "ip", "ports", "endpoints", "route_rules", "destination_policies", "dependencies", "deployments"
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Graph (ApiObject):
    __slots__ = [
        'elements'
    ]

    def __repr__(self):
        return str(self.to_json_object())


class Edge (ApiObject):
    __slots__ = [
        'data'
    ]

    def __repr__(self):
        return str(self.to_json_object())