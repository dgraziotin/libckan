import libckan.model.client as client
import libckan.model.exceptions as exceptions


def term_translation_show(client=client.Client(), terms='', lang_codes=''):
    """
    Return the translations for the given term(s) and language(s).

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param terms: the terms to search for translations of, e.g. ``'Russian'``,
        ``'romantic novel'``
    :type terms: list of strings
    :param lang_codes: the language codes of the languages to search for
        translations into, e.g. ``'en'``, ``'de'`` (optional, default is to
        search for translations into any language)
    :type lang_codes: list of language code strings

    :rtype: a list of term translation dictionaries each with keys ``'term'``
        (the term searched for, in the source language), ``'term_translation'``
        (the translation of the term into the target language) and
        ``'lang_code'`` (the language code of the target language)

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='term_translation_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def vocabulary_list(client=client.Client()):
    """
    Return a list of all the site's tag vocabularies.

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

    resp = client.request(action='vocabulary_list', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def vocabulary_show(client=client.Client(), id=''):
    """
    Return a single tag vocabulary.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param id: the id or name of the vocabulary
    :type id: string
    :return: the vocabulary.
    :rtype: dictionary

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='vocabulary_show', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


def format_autocomplete(client=client.Client(), q='', limit=''):
    """
    Return a list of resource formats whose names contain a string.

    

    :param client: the CKAN Client. 
        Default: an instance of libckan.model.client.Client
    :type client: libckan.model.client.Client
    :param q: the string to search for
    :type q: string
    :param limit: the maximum number of resource formats to return (optional,
        default: 5)
    :type limit: int

    :rtype: list of strings

    

    :returns: the dictionary returned by the CKAN API, 
        with the keys "help","result", and "success". 
        "results" is a list of packages (dict).
    :return: dict

    Raises: :class:`libckan.model.exceptions.CKANError`: 
        An error occurred accessing CKAN API
    """
    args = client.sanitize_params(locals())

    resp = client.request(action='format_autocomplete', data=args)
    if not resp['success']:
        raise exceptions.CKANError(resp.error)
    return resp


