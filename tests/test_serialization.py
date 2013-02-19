__author__ = 'dgraziotin'

from libckan.model import package
from libckan import request


def test_package_retrieval():
    a = request.Api()
    results = a.request(action='package_search',data={'q':'test'})
    del results['help']
    assert results['success'] == True
    assert results['result']['count'] > 0
    assert results['result']['results'] is not None
    p_dict =  results['result']['results'][0]
    assert isinstance(p_dict, dict)
    pkg = package.Package.from_dict(p_dict)
    assert isinstance(pkg, package.Package)
    assert pkg.name != ''


