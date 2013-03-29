import libckan.model.client as client
import libckan.model.exceptions as exceptions


def licence_list(client=client.Client()):
    """
    Return the list of licenses available for datasets on the site.

    :rtype: list of dictionaries

   

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
     

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='licence_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def site_read(client=client.Client()):
    """
    Return ``True``.

    :rtype: boolean

   

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
     

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='site_read', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


