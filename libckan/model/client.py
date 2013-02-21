"""
Lowest communication layer of libckan.
This package contains a wrapper for urllib2 requests that communicates
with CKAN Api. It also contains a Response class to represent CKAN responses.
"""
__author__ = 'dgraziotin'

import urlparse
import urllib2
import urllib
import json
import serializable
import exceptions


#TODO this ugly thing will someday be removed
API_KEY = ''
try:
    import key

    API_KEY = key.key
except ImportError:
    pass


class Response(serializable.Serializable):
    """
    CKAN Action API returns Response objects (in form of JSON).
    We encapsulate it in a Python object for consistency.
    The library actually never returns Response objects.
    It is employed internally.
    """
    def __init__(self):
        self.help = None
        self.result = None
        self.success = None
        self.error = None


class Client(object):
    """
    CKAN API Client. It does HTTP POST request to CKAN API.
    """
    #TODO someday this will come from a config
    _key = API_KEY
    _base_url = 'http://master.ckan.org'

    def __init__(self, base_url=_base_url, api_key=_key):
        self._base_url = base_url
        self._key = api_key

    @classmethod
    def request(cls, action, data=None, base_url=_base_url, api_key=_key):
        """Post a data dict to one of the actions of the CKAN action API.

        Code taken from https://gist.github.com/seanh/4130567

        See the documentation of the action API, including each of
        the available actions and the data dicts they accept, here:
        https://ckan.readthedocs.org/en/255-update-api-docs/api.html

        :param action: the action to post to, e.g. "package_create"
        :type action: str

        :param data: the data to post (optional, default: {})
        :type data: dict

        :param base_url: the base URL of the CKAN instance to post to,
            e.g. "http://datahub.io/"
        :type base_url: str

        :param api_key: the CKAN API key to put in the 'Authorization'
            header of the HTTP request (optional, default: None)
        :type api_key: str

        :returns: the dictionary returned by the CKAN API encapsulated in
            a Response object.
        :return: :class:`libckan.model.client.Response`

        Raises: :class:`libckan.model.exceptions.CKANError`:
            An error occurred accessing CKAN API

        """
        if data is None:
            # Even if you don't want to post any data to the CKAN API, you
            # still have to send an empty dict.
            data = {}
        path = '/api/action/{action}'.format(action=action)
        url = urlparse.urljoin(base_url, path)
        req = urllib2.Request(url)
        resp = None
        if api_key is not None:
            req.add_header('Authorization', api_key)
        try:
            data = json.dumps(data)
            resp = urllib2.urlopen(req, urllib.quote(data))
            # The CKAN API returns a dictionary (in the form of a JSON string)
            # with three keys 'success' (True or False), 'result' and 'help'.
            d = json.loads(resp.read())
            resp = Response.from_dict(d)
            if not resp.success:
                raise exceptions.CKANError(resp.error)
        except urllib2.HTTPError, e:
            # For errors, the CKAN API also returns a dictionary with three
            # keys 'success', 'error' and 'help'.
            error_string = e.read()
            try:
                d = json.loads(error_string)
                if type(d) is unicode:
                    # Sometimes CKAN returns an error as a JSON string not a
                    # dict gloss over it here.
                    resp = Response.from_dict(
                        {'success': False, 'help': '', 'error': d})
                    raise exceptions.CKANError(resp.error)
                resp = Response.from_dict(d)
                if not resp.success:
                    raise exceptions.CKANError(resp.error)
                raise exceptions.CKANError(resp.error)
            except ValueError:
                # Sometimes CKAN returns a string that is not JSON, lets gloss
                # over it.
                resp = Response.from_dict(
                    {'success': False, 'error': error_string, 'help': ''})
                raise exceptions.CKANError(resp.error)
        return resp
