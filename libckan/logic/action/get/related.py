import libckan.model.client as client
import libckan.model.exceptions as exceptions


def related_list(client=client.Client(), id='', dataset='', type_filter='', sort='', featured=''):
    """
    Return a dataset's related items.

    Either the ``id`` or the ``dataset`` parameter must be given.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: id or name of the dataset (optional)
    :type id: string
    :param dataset: dataset dictionary of the dataset (optional)
    :type dataset: dictionary
    :param type_filter: the type of related item to show (optional,
      default: None, show all items)
    :type type_filter: string
    :param sort: the order to sort the related items in, possible values are
      'view_count_asc', 'view_count_desc', 'created_asc' or 'created_desc'
      (optional)
    :type sort: string
    :param featured: whether or not to restrict the results to only featured
      related items (optional, default: False)
    :type featured: bool

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='related_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def related_show(client=client.Client(), id=''):
    """
    Return a single related item.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id of the related item to show
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

    resp = client.request(action='related_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


