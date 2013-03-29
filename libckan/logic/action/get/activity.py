import libckan.model.client as client
import libckan.model.exceptions as exceptions


def dashboard_activity_list(client=client.Client(), offset='', limit=''):
    """
    Return the authorized user's dashboard activity stream.

    Unlike the activity dictionaries returned by other ``*_activity_list``
    actions, these activity dictionaries have an extra boolean value with key
    ``is_new`` that tells you whether the activity happened since the user last
    viewed her dashboard (``'is_new': True``) or not (``'is_new': False``).

    The user's own activities are always marked ``'is_new': False``.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ``ckan.activity_list_limit`` setting)

    :rtype: list of activity dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='dashboard_activity_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def dashboard_activity_list_html(client=client.Client(), offset='', limit=''):
    """
    Return the authorized user's dashboard activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='dashboard_activity_list_html', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def dashboard_new_activities_count(client=client.Client()):
    """
    Return the number of new activities in the user's dashboard.

    Return the number of new activities in the authorized user's dashboard
    activity stream.

    Activities from the user herself are not counted by this function even
    though they appear in the dashboard (users don't want to be notified about
    things they did themselves).

    :rtype: int

   

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

    resp = client.request(action='dashboard_new_activities_count', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def activity_detail_list(client=client.Client(), id=''):
    """
    Return an activity's list of activity detail items.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id of the activity
    :type id: string
    :rtype: list of dictionaries.

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='activity_detail_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def group_activity_list(client=client.Client(), id='', offset='', limit=''):
    """
    Return a group's activity stream.

    You must be authorized to view the group.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the group
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
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

    resp = client.request(action='group_activity_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def group_activity_list_html(client=client.Client(), id='', offset='', limit=''):
    """
    Return a group's activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the group
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='group_activity_list_html', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def organization_activity_list(client=client.Client(), id=''):
    """
    Return a organization's activity stream.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the organization
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

    resp = client.request(action='organization_activity_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def organization_activity_list_html(client=client.Client(), id=''):
    """
    Return a organization's activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the organization
    :type id: string

    :rtype: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='organization_activity_list_html', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_activity_list(client=client.Client(), id='', offset='', limit=''):
    """
    Return a package's activity stream.

    You must be authorized to view the package.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the package
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
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

    resp = client.request(action='package_activity_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def package_activity_list_html(client=client.Client(), id='', offset='', limit=''):
    """
    Return a package's activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the package
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='package_activity_list_html', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def user_activity_list(client=client.Client(), id='', offset='', limit=''):
    """
    Return a user's public activity stream.

    You must be authorized to view the user's profile.


    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the user
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
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

    resp = client.request(action='user_activity_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def user_activity_list_html(client=client.Client(), id='', offset='', limit=''):
    """
    Return a user's public activity stream as HTML.

    The activity stream is rendered as a snippet of HTML meant to be included
    in an HTML page, i.e. it doesn't have any HTML header or footer.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: The id or name of the user.
    :type id: string
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='user_activity_list_html', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def recently_changed_packages_activity_list(client=client.Client(), offset='', limit=''):
    """
    Return the activity stream of all recently added or changed packages.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
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

    resp = client.request(action='recently_changed_packages_activity_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def recently_changed_packages_activity_list_html(client=client.Client(), offset='', limit=''):
    """
    Return the activity stream of all recently changed packages as HTML.

    The activity stream includes all recently added or changed packages. It is
    rendered as a snippet of HTML meant to be included in an HTML page, i.e. it
    doesn't have any HTML header or footer.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param offset: where to start getting activity items from
        (optional, default: 0)
    :type offset: int
    :param limit: the maximum number of activities to return
        (optional, default: 31, the default value is configurable via the
        ckan.activity_list_limit setting)
    :type limit: int

    :rtype: string

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='recently_changed_packages_activity_list_html', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


