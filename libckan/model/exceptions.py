"""
libckan custom exceptions are defined in this module.
"""


class CKANError(Exception):
    """
    General CKAN API error. It encapsulates the error part of a CKAN Response.
    """
    def __init__(self, response_error):
        try:
            message = response_error['message']
            type = response_error['__type']
        except (KeyError, TypeError):
            message = str(response_error)
            type = 'Unknown Error'
        super(Exception, self).__init__(message)
        self.type = type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.type) + ": " + str(self.message)


class CKANAccessError(CKANError):
    """
    Errors related to authentication (i.e., access denied)
    """
    pass


class CKANValidationError(CKANError):
    """
    Errors related to Validation issues.
    """
    pass




