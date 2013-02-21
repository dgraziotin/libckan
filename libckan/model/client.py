__author__ = 'dgraziotin'

import serializable
import exceptions
import urlparse
import urllib2
import urllib
import json



#TODO this ugly thing will someday be removed
API_KEY = ''
try:
    import key
    API_KEY = key.key
except ImportError:
    API_KEY = ''


class Response(serializable.Serializable):
    """

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
    _key = API_KEY                          #TODO someday this will come from a config
    _base_url = 'http://master.ckan.org'    #TODO someday this will come from a config

    def __init__(self, base_url=_base_url, api_key=_key):
        self._base_url = base_url
        self._key = api_key

    @classmethod
    def request(cls, action, data=None, base_url=_base_url, api_key=_key):
        """Post a data dict to one of the actions of the CKAN action API.

        See the documentation of the action API, including each of the available
        actions and the data dicts they accept, here:
        http://docs.ckan.org/en/ckan-1.8/apiv3.html

        :param base_url: the base URL of the CKAN instance to post to,
            e.g. "http://datahub.io/"
        :type base_url: string

        :param action: the action to post to, e.g. "package_create"
        :type action: string

        :param data: the data to post (optional, default: {})
        :type data: dictionary

        :param api_key: the CKAN API key to put in the 'Authorization' header of
            the HTTP request (optional, default: None)
        :type api_key: string

        :returns: the dictionary returned by the CKAN API, a dictionary with three
            keys 'success' (True or False), 'help' (the docstring for the action
            posted to) and 'result' in the case of a successful request or 'error'
            in the case of an unsuccessful request
        :return: dictionary

        """
        if data is None:
            # Even if you don't want to post any data to the CKAN API, you still
            # have to send an empty dict.
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
                    # Sometimes CKAN returns an error as a JSON string not a dict,
                    # gloss over it here.
                    resp = Response.from_dict({'success': False, 'help': '', 'error': d})
                    raise exceptions.CKANError(resp.error)
                resp = Response.from_dict(d)
                if not resp.success:
                    raise exceptions.CKANError(resp.error)
                raise exceptions.CKANError(resp.error)
            except ValueError:
                # Sometimes CKAN returns a string that is not JSON, lets gloss
                # over it.
                resp = Response.from_dict({'success': False, 'error': error_string, 'help': ''})
                raise exceptions.CKANError(resp.error)
        return resp
