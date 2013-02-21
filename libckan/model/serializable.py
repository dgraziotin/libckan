__author__ = 'dgraziotin'


class Serializable(object):
    """
    Superclass for all libckan models related to CKAN API models. A mix between an Abstract Class and an Interface.
    Never instantiate it.
    """

    def __init__(self):
        raise NotImplementedError("Please do not directly instantiate Serializable")

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Return a CKAN Python object, given the related CKAN dict (converted from CKAN JSON).
        This method is suitable for all trivial CKAN API objects.

        :param obj_dict: the CKAN Client. Default: an instance of libckan.model.client.Client
        :type obj_dict: dict

        :returns: a libckan API Python object.
        :rtype: :class:`libckan.model.serializable.Serializable`

        :raises: ValueError if obj_dict is not a dict
        """
        if not isinstance(obj_dict, dict):
            raise ValueError('Please use Python dict objects to generate libckan objects.')

        obj = cls()
        for key in obj_dict.keys():
            if key in obj.__dict__:
                obj.__dict__[key] = obj_dict[key]
        return obj

    @classmethod
    def to_dict(cls):
        raise NotImplementedError("Please do not directly use Serializable")