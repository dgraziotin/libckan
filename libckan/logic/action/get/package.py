import libckan.model.client as client
import libckan.model.exceptions as exceptions


def package_autocomplete(client=client.Client(), q=''):
    """
    Return a list of datasets (packages) that match a string.

    Datasets with names or titles that contain the query string will be
    returned.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param q: the string to search for
    :type q: string

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='package_autocomplete', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_list(client=client.Client()):
    """
    Return a list of the names of the site's datasets (packages).

    :rtype: list of strings


    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client

    :returns: A list of names of the packages.
    :return: [str]

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='package_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_relationships_list(client=client.Client(), id='', id2='', rel=''):
    """
    Return a dataset (package)'s relationships.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the package
    :type id: string
    :param id2:
    :type id2:
    :param rel:
    :type rel:

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='package_relationships_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_search(client=client.Client(), q='', fq='', rows='', sort='', start='', qf='', facet='', facet_mincount='', facet_limit='', facet_field='', count='', results='', facets='', search_facets=''):
    """
    
    Searches for packages satisfying a given search criteria.

    This action accepts solr search query parameters (details below), and
    returns a dictionary of results, including dictized datasets that match
    the search criteria, a search count and also facet information.

    **Solr Parameters:**

    For more in depth treatment of each paramter, please read the `Solr
    Documentation <http://wiki.apache.org/solr/CommonQueryParameters>`_.

    This action accepts a *subset* of solr's search query parameters:

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param q: the solr query.  Optional.  Default: `"*:*"`
    :type q: string
    :param fq: any filter queries to apply.  Note: `+site_id:{ckan_site_id}`
        is added to this string prior to the query being executed.
    :type fq: string
    :param rows: the number of matching rows to return.
    :type rows: int
    :param sort: sorting of the search results.  Optional.  Default:
        "score desc, name asc".  As per the solr documentation, this is a
        comma-separated string of field names and sort-orderings.
    :type sort: string
    :param start: the offset in the complete result for where the set of
        returned datasets should begin.
    :type start: int
    :param qf: the dismax query fields to search within, including boosts.  See
        the `Solr Dismax Documentation
        <http://wiki.apache.org/solr/DisMaxQParserPlugin#qf_.28Query_Fields.29>`_
        for further details.
    :type qf: string
    :param facet: whether to enable faceted results.  Default: "true".
    :type facet: string
    :param facet.mincount: the minimum counts for facet fields should be
        included in the results.
    :type facet.mincount: int
    :param facet.limit: the maximum number of constraint counts that should be
        returned for the facet fields. A negative value means unlimited
    :type facet.limit: int
    :param facet.field: the fields to facet upon.  Default empty.  If empty,
        then the returned facet information is empty.
    :type facet.field: list of strings

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    **Results:**

    The result of this action is a dict with the following keys:

    :rtype: A dictionary with the following keys
    :param count: the number of results found.  Note, this is the total number
        of results found, not the total number of results returned (which is
        affected by limit and row parameters used in the input).
    :type count: int
    :param results: ordered list of datasets matching the query, where the
        ordering defined by the sort parameter used in the query.
    :type results: list of dictized datasets.
    :param facets: DEPRECATED.  Aggregated information about facet counts.
    :type facets: DEPRECATED dict
    :param search_facets: aggregated information about facet counts.  The outer
        dict is keyed by the facet field name (as used in the search query).
        Each entry of the outer dict is itself a dict, with a "title" key, and
        an "items" key.  The "items" key's value is a list of dicts, each with
        "count", "display_name" and "name" entries.  The display_name is a
        form of the name that can be used in titles.
    :type search_facets: nested dict of dicts.

    An example result: ::

     {'count': 2,
      'results': [ { <snip> }, { <snip> }],
      'search_facets': {u'tags': {'items': [{'count': 1,
                                             'display_name': u'tolstoy',
                                             'name': u'tolstoy'},
                                            {'count': 2,
                                             'display_name': u'russian',
                                             'name': u'russian'}
                                           ]
                                 }
                       }
     }

    **Limitations:**

    The full solr query language is not exposed, including.

    fl
        The parameter that controls which fields are returned in the solr
        query cannot be changed.  CKAN always returns the matched datasets as
        dictionary objects.

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='package_search', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_show(client=client.Client(), id=''):
    """
    Return the metadata of a dataset (package) and its resources.


    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the dataset
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

    resp = client.request(action='package_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def current_package_list_with_resources(client=client.Client(), limit='', page=''):
    """
    Return a list of the site's datasets (packages) and their resources.

    The list is sorted most-recently-modified first.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param limit: if given, the list of datasets will be broken into pages of
        at most ``limit`` datasets per page and only one page will be returned
        at a time (optional)
    :type limit: int
    :param page: when ``limit`` is given, which page to return
    :type page: int

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='current_package_list_with_resources', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def group_package_show(client=client.Client(), id='', limit=''):
    """
    Return the datasets (packages) of a group.


    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the group
    :type id: string
    :param limit: the maximum number of datasets to return (optional)
    :type limit: int

    :rtype: list of dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='group_package_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


