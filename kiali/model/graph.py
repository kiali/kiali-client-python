from kiali.model.apiObject import ApiObject


class Graph (ApiObject):
    __slots__ = [
        'elements'
    ]

    def __repr__(self):
        return str(self.to_json_object())
