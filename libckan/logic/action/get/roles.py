import libckan.model.client as client
import libckan.model.exceptions as exceptions


def roles_show(client=client.Client(), domain_object='', user=''):
    """
    Return the roles of all users and authorization groups for an object.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param domain_object: a package or group name or id
        to filter the results by
    :type domain_object: string
    :param user: a user name or id
    :type user: string

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='roles_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def member_roles_list(client=client.Client()):
    """
    <TODO: DESCRIPTION>

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    <TODO: PARAMETERS>

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='member_roles_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


