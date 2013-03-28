import libckan.model.client as client
import libckan.model.exceptions as exceptions


def status_show(client=client.Client()):
    """
    Return a dictionary with information about the site's configuration

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    .

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='status_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def resource_status_show(client=client.Client(), id=''):
    """
    Return the statuses of a resource's tasks.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id of the resource
    :type id: string

    :rtype: list of (status, date_done, traceback, task_status) dictionaries

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='resource_status_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def task_status_show(client=client.Client(), id='', entity_id='', task_type='', key=''):
    """
    Return a task status.

    Either the ``id`` parameter *or* the ``entity_id``, ``task_type`` *and*
    ``key`` parameters must be given.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id of the task status (optional)
    :type id: string
    :param entity_id: the entity_id of the task status (optional)
    :type entity_id: string
    :param task_type: the task_type of the task status (optional)
    :type tast_type: string
    :param key: the key of the task status (optional)
    :type key: string

    :rtype: dictionary

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='task_status_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


