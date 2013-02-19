import request

__author__ = 'dgraziotin'

import urllib2
import nose.tools

def test_request_non_existing_action():
    a = request.Api()
    results = a.request(action='non_existing')
    assert results['success'] is False

def test_request_existing_action():
    a = request.Api()
    results = a.request(action='package_search')
    assert results['success'] is True

def test_request_wrong_data():
    a = request.Api()
    results = a.request(action='package_search', data=123)
    assert results['success'] is False

def test_request_ok_data():
    a = request.Api()
    results = a.request(action='package_search',data={'q':'test'})
    assert results['success'] is True


def test_request_valid_api_key():
    a = request.Api()
    results = a.request(action='am_following_user',data={'id':'idonotexisthopefully123'})
    assert results['success'] is False

def test_request_nonvalid_api_key():
    a = request.Api()
    results = a.request(action='am_following_user',data={'id':'dgraziotin'},api_key='ravioli ravioli give me the formuoli')
    assert results['success'] is False
    assert results['error']['message'] is not None

@nose.tools.raises(ValueError)
def test_request_malformed_url():
    a = request.Api()
    results = a.request(action='package_search',data={'q':'test'},base_url='htt://hai;notgood')

@nose.tools.raises(urllib2.URLError)
def test_request_url_error():
    a = request.Api()
    results = a.request(action='package_search',data={'q':'test'},base_url='http://okfn-i-love;it')
