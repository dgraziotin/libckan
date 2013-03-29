import libckan.model.client as client
import libckan.model.exceptions as exceptions


def revision_list(client=client.Client()):
    """
    Return a list of the IDs of the site's revisions.

    :rtype: list of strings

   

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

    resp = client.request(action='revision_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def revision_show(client=client.Client(), id=''):
    """
    Return the details of a revision.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id of the revision
    :type id: string

    :rtype: dictionary

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='revision_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_revision_list(client=client.Client(), id=''):
    """
    Return a dataset (package)'s revisions as a list of dictionaries.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the dataset
    :type id: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='package_revision_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def group_revision_list(client=client.Client(), id=''):
    """
    Return a group's revisions.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the name or id of the group
    :type id: string

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='group_revision_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


