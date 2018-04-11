from kiali.model.apiObject import ApiObject


class Namespace(ApiObject):
    __slots__ = [
        'name'
    ]

    def __repr__(self):
        return str(self.to_json_object())

