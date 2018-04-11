try:
    import simplejson as json
except ImportError:
    import json


class ApiObject(object):

    __slots__ = []

    defaults = dict()

    def __init__(self, dictionary=dict()):
        udict = ApiObject.transform_dict_to_underscore(dictionary)
        for k in self.__slots__:
            setattr(self, k, udict.get(k,self.defaults.get(k)))

    def to_json_object(self):
        dictionary = {}
        for attribute in self.__slots__:
            if hasattr(self,attribute):
                dictionary[attribute] = getattr(self,attribute)
        return ApiObject.transform_dict_to_camelcase(dictionary)

    @staticmethod
    def _to_camelcase(word):
        s = ''.join(x.capitalize() or '_' for x in word.split('_'))
        return ''.join([s[0].lower(), s[1:]])

    @staticmethod
    def _to_underscore(word):
        return ''.join(["_" + c.lower() if c.isupper() else c for c in word]).strip('_')

    @staticmethod
    def transform_dict_to_camelcase(dictionary):
        if dictionary is None:
            return dict()
        return dict((ApiObject._to_camelcase(k), v) for k, v in dictionary.items() if v is not None)

    @staticmethod
    def transform_dict_to_underscore(dictionary):
        if dictionary is None:
            return dict()
        return dict((ApiObject._to_underscore(k), v) for k, v in dictionary.items() if v is not None)

    @classmethod
    def list_to_object_list(cls, o):
        if o is not None:
            return [cls(ob) for ob in o]
        return []

class ApiJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ApiObject):
            return obj.to_json_object()
        else:
            return json.JSONEncoder.default(self, obj)