import libckan.model.client as client
import libckan.model.exceptions as exceptions


def site_read(client=client.Client()):
    """
    This method always returns True.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is always True (bool)
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: An error occurred
        accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='site_read', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_search(client=client.Client(), q='*:*', fq='', rows=20,
                   sort='score desc, name asc', start=0, qf='',
                   facet=True, facet_mincount='', facet_limit='',
                   facet_field=''):
    """Search for packages satisfying a given search criteria.

    This action accepts solr search query parameters (details below), and
    returns a list of Packages that match the search criteria

    **Solr Parameters:**

    For more in depth treatment of each paramter, please read the `Solr
    Documentation <http://wiki.apache.org/solr/CommonQueryParameters>`_.

    This action accepts a *subset* of solr's search query parameters:

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
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
        <http://wiki.apache.org/solr/DisMaxQParserPlugin>`_
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

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list of datasets (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='package_search', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_list(client=client.Client()):
    """
    Return a list of the names of the site's datasets (packages).

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success".
        "results" is a list of package names (unicode str).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    resp = client.request(action='package_list')
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def current_package_list_with_resources(client=client.Client(), limit=None,
                                        page=None):
    """Return a list of the site's datasets (packages) and their resources.

    The list is sorted most-recently-modified first.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param limit: if given, the list of datasets will be broken into pages of
        at most ``limit`` datasets per page and only one page will be returned
        at a time (optional)
    :type limit: int
    :param page: when ``limit`` is given, which page to return
    :type page: int

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='current_package_list_with_resources',
                          data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def revision_list(client=client.Client()):
    """Return a list of the IDs of the site's revisions.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list of IDs ([unicode str]).
    :return: list of unicode str

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='revision_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_revision_list(client=client.Client(), id=''):
    """Return a dataset (package)'s revisions as a list of dictionaries.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the dataset
    :type id: string

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list of Package revisions
            ([dict]) each one containing the elements "timestamp", "messsage",
            "approved_timestamp", "id", and "author"
    :return: list of dicts

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='package_revision_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def related_show(client=client.Client(), id=''):
    """Return an item related to the provided one.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id of the related item to show
    :type id: str

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a related items
    :return: list of dict

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='related_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def related_list(client=client.Client(), id='', type_filter=None,
                 sort=None, featured=False):
    """Return a dataset's related items.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: id or name of the dataset
    :type id: string
    :param type_filter: the type of related item to show (optional,
      default: None, show all items)
    :type type_filter: str
    :param sort: the order to sort the related items in, possible values are
      'view_count_asc', 'view_count_desc', 'created_asc' or 'created_desc'
      (optional)
    :type sort: str
    :param featured: whether or not to restrict the results to only featured
      related items (optional, default: False)
    :type featured: bool

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list dicts.
    :return: list of dict

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='related_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def member_list(client=client.Client(), id='', object_type=None,
                param_capacity=None):
    """Return the members of a group.

    The user must have permission to 'get' the group.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: id of the group
    :type id: str
    :param object_type: restrict the members returned to those of a given type,
      e.g. ``'user'`` or ``'package'`` (optional, default: ``None``)
    :type object_type: str
    :param capacity: restrict the members returned to those with a given
      capacity, e.g. ``'member'``, ``'editor'``, ``'admin'``, ``'public'``,
      ``'private'`` (optional, default: ``None``)
    :type capacity: str

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list dicts.
    :return: list of (id, type, capacity) tuples

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    #TODO won't work unless https://github.com/okfn/ckan/issues/623 is fixed
    raise NotImplementedError("Currently not working in CKAN 2.0")

#    args = _sanitize(locals())
#
#    resp = client.request(action='member_list', data=args)
#    if not resp['success']:
#        raise exceptions.CKANError(resp.error)
#    return resp


def group_list(client=client.Client(), sort=None, groups=None,
               all_fields=False):
    """Return a list of the names of the site's groups.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param sort: sorting of the search results.  Optional.  Default:
        "name asc" string of field name and sort-order. The allowed fields are
        'name' and 'packages'
    :type sort: str
    :param groups: a list of names of the groups to return, if given only
        groups whose names are in this list will be returned (optional)
    :type groups: list of str
    :param all_fields: return full group dictionaries instead of  just names
        (optional, default: ``False``)
    :type all_fields: bool

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list dicts.
    :return: list of (id, type, capacity) tuples

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='group_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def organization_list(client=client.Client(), sort=None, organizations=None,
                      all_fields=False):
    """Return a list of the names of the site's organizations.

    :param client: the CKAN Client. Default: an instance of
        libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param sort: sorting of the search results.  Optional.  Default:
        "name asc" string of field name and sort-order. The allowed fields are
        'name' and 'packages'
    :type sort: str
    :param organizations: a list of names of the groups to return, if given only
        groups whose names are in this list will be returned (optional)
    :type organizations: list of str
    :param all_fields: return full group dictionaries instead of  just names
        (optional, default: ``False``)
    :type all_fields: bool

    :returns: the dictionary returned by the CKAN API, with the keys "help",
        "result", and "success". "results" is a list dicts.
    :return: list of (id, type, capacity) tuples

    Raises: :class:`libckan.model.exceptions.CKANError`:
        An error occurred accessing CKAN API
    """
    args = _sanitize(locals())

    resp = client.request(action='organization_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def _sanitize(params):
    """
    Polishes the parameters to be sent to CKAN.

    :param params: A dict of parameters. Usually obtained with a call
    to :func:`locals`
    :type client: dict

    :returns: The sanitizied dict of parameters
    :rtype: dict
    """

    if not isinstance(params, dict):
        raise TypeError('_sanitize(params) needs a dict as parameter')

    params_copy = params.copy()

    for key in params.keys():
        if (params[key] is None or params[key] == ''
                or key in ["self", "cls", "client", "args"]):
            del params_copy[key]

    for key in params.keys():
        if key.startswith('facet_'):
            new_key = key.replace('_', '.')
            params_copy[new_key] = params[key]
            del params[key]
        if key == 'facet':
            params_copy[key] = str(params[key]).lower()

    return params_copy
