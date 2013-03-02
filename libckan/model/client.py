"""
Lowest communication layer of libckan.
This package contains a wrapper for urllib2 requests that communicates
with CKAN Api. It also contains a Response class to represent CKAN responses.
"""
import urlparse
import urllib2
import urllib
import json
import exceptions


#TODO this ugly thing will someday be removed
API_KEY = ''
try:
    import key

    API_KEY = key.key
except ImportError:
    pass


class Client(object):
    """
    CKAN API Client. It does HTTP POST request to CKAN API.
    """
    #TODO someday this will come from a config
    _key = API_KEY
    _base_url = 'http://beta.ckan.org'

    def __init__(self, base_url=_base_url, api_key=_key):
        self._base_url = base_url
        self._key = api_key

    @classmethod
    def request(cls, action, data=None, base_url=_base_url, api_key=_key):
        """Post a data dict to one of the actions of the CKAN action API.

        Code adapted from https://gist.github.com/seanh/4130567

        :param action: the action to post to, e.g. "package_create"
        :type action: str

        :param data: the data to post (optional, default: {})
        :type data: dict

        :param base_url: the base URL of the CKAN instance to post to,
            e.g. "http://datahub.io/"
        :type base_url: str

        :param api_key: the CKAN API key to put in the 'Authorization'
            header of the HTTP request (optional, default: '')
        :type api_key: str

        :returns: the dictionary returned by the CKAN API
        :return: dict

        Raises: :class:`libckan.model.exceptions.CKANError`:
            An error occurred accessing CKAN API
        """
        if data is None:
            # Even if you don't want to post any data to the CKAN API, you
            # still have to send an empty dict.
            data = {}
        path = '/api/action/{action}'.format(action=action)
        url = urlparse.urljoin(base_url, path)
        request = urllib2.Request(url)
        if api_key is not None:
            request.add_header('Authorization', api_key)
        try:
            response = urllib2.urlopen(request, urllib.quote(json.dumps(data)))
            # The CKAN API returns a dictionary (in the form of a JSON string)
            # with three keys 'success' (True or False), 'result' and 'help'.
            results_dict = json.loads(response.read())
            if results_dict['success'] is False:
                raise exceptions.CKANError(results_dict['error'])
            return results_dict
        except urllib2.HTTPError, e:
            # For errors, the CKAN API also returns a dictionary with three
            # keys 'success', 'error' and 'help'.
            error_string = e.read()
            try:
                results_dict = json.loads(error_string)
                if type(results_dict) is unicode:
                    # Sometimes CKAN returns an error as a JSON string
                    # not a dict, gloss over it here.
                    raise exceptions.CKANError(results_dict)
                if results_dict['success'] is False:
                    raise exceptions.CKANError(results_dict['error'])
                return results_dict
            except ValueError:
                # Sometimes CKAN returns a string that is not JSON, lets gloss
                # over it.
                raise exceptions.CKANError(error_string)
