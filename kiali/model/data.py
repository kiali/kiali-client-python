from kiali.model.apiObject import ApiObject


class Data (ApiObject):
    __slots__ = [
        'id', "source", "target", "version", "text", "color", "style", "rate", "service"
    ]

    def __repr__(self):
        return str(self.to_json_object())

