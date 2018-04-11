from kiali.model.apiObject import ApiObject


class Elements (ApiObject):
    __slots__ = [
        'nodes', "edges"
    ]

    def __repr__(self):
        return str(self.to_json_object())
