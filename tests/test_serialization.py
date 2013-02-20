__author__ = 'dgraziotin'

from libckan.model import package
from libckan.model import client



def test_package_retrieval():
    a = client.Client()
    results = a.request(action='package_search',data={'q':'test'})
    assert results.success == True
    assert results.result['count'] > 0
    assert results.result['results'] is not None

    assert isinstance(results, client.Response)
    assert isinstance(results.result['results'][0], dict)
    assert results.result['results'][0]['name'] != ''


