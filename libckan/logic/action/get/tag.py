import libckan.model.client as client
import libckan.model.exceptions as exceptions


def tag_autocomplete(client=client.Client(), query='', vocabulary_id='', fields='', limit='', offset=''):
    """
    Return a list of tag names that contain a given string.

    By default only free tags (tags that don't belong to any vocabulary) are
    searched. If the ``vocabulary_id`` argument is given then only tags
    belonging to that vocabulary will be searched instead.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param query: the string to search for
    :type query: string
    :param vocabulary_id: the id or name of the tag vocabulary to search in
      (optional)
    :type vocabulary_id: string
    :param fields: deprecated
    :type fields: dictionary
    :param limit: the maximum number of tags to return
    :type limit: int
    :param offset: when ``limit`` is given, the offset to start returning tags
        from
    :type offset: int

    :rtype: list of strings

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='tag_autocomplete', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def tag_list(client=client.Client(), query='', vocabulary_id='', all_fields=''):
    """
    Return a list of the site's tags.

    By default only free tags (tags that don't belong to a vocabulary) are
    returned. If the ``vocabulary_id`` argument is given then only tags
    belonging to that vocabulary will be returned instead.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param query: a tag name query to search for, if given only tags whose
        names contain this string will be returned (optional)
    :type query: string
    :param vocabulary_id: the id or name of a vocabulary, if give only tags
        that belong to this vocabulary will be returned (optional)
    :type vocabulary_id: string
    :param all_fields: return full tag dictionaries instead of just names
        (optional, default: ``False``)
    :type all_fields: boolean

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='tag_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def tag_search(client=client.Client(), query='', vocabulary_id='', fields='', limit='', offset=''):
    """
    Return a list of tags whose names contain a given string.

    By default only free tags (tags that don't belong to any vocabulary) are
    searched. If the ``vocabulary_id`` argument is given then only tags
    belonging to that vocabulary will be searched instead.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param query: the string(s) to search for
    :type query: string or list of strings
    :param vocabulary_id: the id or name of the tag vocabulary to search in
      (optional)
    :type vocabulary_id: string
    :param fields: deprecated
    :type fields: dictionary
    :param limit: the maximum number of tags to return
    :type limit: int
    :param offset: when ``limit`` is given, the offset to start returning tags
        from
    :type offset: int

    :returns: A dictionary with the following keys:

      ``'count'``
        The number of tags in the result.

      ``'results'``
        The list of tags whose names contain the given string, a list of
        dictionaries.

    :rtype: dictionary

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='tag_search', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def tag_show(client=client.Client(), id=''):
    """
    Return the details of a tag and all its datasets.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the name or id of the tag
    :type id: string

    :returns: the details of the tag, including a list of all of the tag's
        datasets and their details
    :rtype: dictionary

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='tag_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp




