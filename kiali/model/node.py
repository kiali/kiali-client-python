from kiali.model.apiObject import ApiObject


class Node (ApiObject):
    __slots__ = [
        'data'
    ]

    def __repr__(self):
        return str(self.to_json_object())
