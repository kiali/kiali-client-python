from kiali.model.apiObject import ApiObject


class Rule(ApiObject):
    __slots__ = [
        'name', 'match', 'actions', 'instances', 'namespace'
    ]

    def __repr__(self):
        return str(self.to_json_object())

