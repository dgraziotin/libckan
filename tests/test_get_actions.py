__author__ = 'dgraziotin'

import libckan.logic.action.get
import libckan.model.package


def test_package_search_non_existing():
    results = libckan.logic.action.get.package_search(q='idonotexisth0pefllt123')
    assert results == []


def test_package_search():
    results = libckan.logic.action.get.package_search(q='test')
    assert type(results) is type([])
    assert isinstance(results[0], libckan.model.package.Package)


def test_package_list():
    results = libckan.logic.action.get.package_list()
    assert type(results) is type([])
    assert isinstance(results[0], libckan.model.package.Package)