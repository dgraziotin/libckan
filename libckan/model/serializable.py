__author__ = 'dgraziotin'


class Serializable(object):

    def __init__(self):
        raise NotImplementedError("Please do not directly instantiate Serializable")

    @staticmethod
    def from_dict(dict):
        raise NotImplementedError("Please do not directly use Serializable")

    @staticmethod
    def to_dict():
        raise NotImplementedError("Please do not directly use Serializable")