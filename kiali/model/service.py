from kiali.model.apiObject import ApiObject


class Service (ApiObject):
    __slots__ = [
        'name', 'replicas', 'available_replicas', 'unavailable_replicas', 'istio_sidecar', 'request_count', 'request_error_count', 'error_rate',
        "labels", "type", "ip", "ports", "endpoints", "route_rules", "destination_policies", "dependencies", "deployments"
    ]

    def __repr__(self):
        return str(self.to_json_object())

