__author__ = 'dgraziotin'

from libckan.logic.action import get
from libckan.model import package


def test_package_search_non_existing():
    res = get.Package().search(q='idonotexisthopefully123321')
    assert res.success is True
    assert res.result['count'] == 0


def test_package_search():
    res = get.Package().search(q='test')
    assert res.success is True
    assert res.result['count'] > 0
    assert isinstance(res.result['results'][0], package.Package)