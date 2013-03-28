import libckan.model.client as client
import libckan.model.exceptions as exceptions


def organization_list(client=client.Client(), order_by='', sort='', organizations='', all_fields=''):
    """
    Return a list of the names of the site's organizations.

    

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
    :param organizations: a list of names of the groups to return, if given only
        groups whose names are in this list will be returned (optional)
    :type organizations: list of strings
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

    resp = client.request(action='organization_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def organization_list_for_user(client=client.Client(), permission=''):
    """
    Return the list of organizations that the user is a member of.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param permission: the permission the user has against the returned organizations
      (optional, default: ``edit_group``)
    :type permission: string

    :returns: the names of organizations the user is authorized to do specific permission
    :rtype: list of strings

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='organization_list_for_user', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def organization_show(client=client.Client(), id=''):
    """
    Return the details of a organization.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the organization
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

    resp = client.request(action='organization_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


