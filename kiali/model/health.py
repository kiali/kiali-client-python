from kiali.model.apiObject import ApiObject


class Health (ApiObject):
    __slots__ = [
        'healthy_replicas', 'total_replicas'
    ]

    def __repr__(self):
        return str(self.to_json_object())

