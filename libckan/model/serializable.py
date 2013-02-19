__author__ = 'dgraziotin'


class Serializable(object):

    def __init__(self):
        raise NotImplementedError("Please do not directly instantiate Serializable")

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        for key in dict.keys():
            if key in obj.__dict__:
                obj.__dict__[key] = dict[key]
        return obj

    @classmethod
    def to_dict(cls):
        raise NotImplementedError("Please do not directly use Serializable")