import urllib2
import nose.tools
import libckan.model.client as client
import libckan.model.exceptions as exceptions


@nose.tools.raises(exceptions.CKANError)
def test_request_non_existing_action():
    a = client.Client()
    results = a.request(action='non_existing')
    assert results['success'] is False


def test_request_existing_action():
    a = client.Client()
    results = a.request(action='package_search')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_request_wrong_data():
    a = client.Client()
    results = a.request(action='package_search', data=123)
    assert results['success'] is False


def test_request_ok_data():
    a = client.Client()
    results = a.request(action='package_search',data={'q':'test'})
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_request_valid_client_key():
    a = client.Client()
    results = a.request(action='am_following_user',data={'id':'idonotexisthopefully123'})
    print results
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_request_nonvalid_client_key():
    a = client.Client(api_key='ravioli ravioli give me the formuoli')
    results = a.request(action='am_following_user',data={'id':'dgraziotin'})
    assert results['success'] is False


@nose.tools.raises(ValueError)
def test_request_malformed_url():
    a = client.Client()
    results = a.request(action='package_search',data={'q':'test'},base_url='htt://hai;notgood')


@nose.tools.raises(urllib2.URLError)
def test_request_url_error():
    a = client.Client()
    results = a.request(action='package_search',data={'q':'test'},base_url='http://okfn-i-love;it')