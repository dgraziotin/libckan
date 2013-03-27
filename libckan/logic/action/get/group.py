import libckan.model.client as client
import libckan.model.exceptions as exceptions


def group_list(client=client.Client(), order_by='', sort='', groups='', all_fields=''):
    """
    Return a list of the names of the site's groups.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param order_by: the field to sort the list by, must be ``'name'`` or
      ``'packages'`` (optional, default: ``'name'``) Deprecated use sort.
    :type order_by: string
    :param sort: sorting of the search results.  Optional.  Default:
        "name asc" string of field name and sort-order. The allowed fields are
        'name' and 'packages'
    :type sort: string
    :param groups: a list of names of the groups to return, if given only
        groups whose names are in this list will be returned (optional)
    :type groups: list of strings
    :param all_fields: return full group dictionaries instead of  just names
        (optional, default: ``False``)
    :type all_fields: boolean

    :rtype: list of strings

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='group_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def group_list_authz(client=client.Client(), available_only=''):
    """
    Return the list of groups that the user is authorized to edit.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param available_only: remove the existing groups in the package
      (optional, default: ``False``)
    :type available_only: boolean

    :returns: the names of groups that the user is authorized to edit
    :rtype: list of strings

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='group_list_authz', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def group_show(client=client.Client(), id=''):
    """
    Return the details of a group.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the group
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

    resp = client.request(action='group_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


