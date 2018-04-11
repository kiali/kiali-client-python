from kiali.model.apiObject import ApiObject


class Metric (ApiObject):
    __slots__ = [
        'request_count_in', "request_count_out", "request_error_count_in", "request_error_count_out"
    ]

    def __repr__(self):
        return str(self.to_json_object())

