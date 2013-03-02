import libckan.logic.action.get


def test_site_read():
    results = libckan.logic.action.get.site_read()
    assert results['success'] is True
    assert results['result'] is True


def test_package_search_non_existing():
    results = libckan.logic.action.get.package_search(
        q='idonotexisth0pefllt123')
    assert results['success'] is True
    assert results['result']['count'] == 0
    assert results['result']['results'] == []


def test_package_search():
    results = libckan.logic.action.get.package_search(q='test')
    assert results['success'] is True
    assert results['result']['count'] > 0
    assert len(results['result']['results']) > 0


def test_package_list():
    results = libckan.logic.action.get.package_list()
    assert results['success'] is True
    assert len(results['result']) > 0


def test_current_package_list_with_resources():
    results = libckan.logic.action.get.current_package_list_with_resources()
    assert results['success'] is True
    assert len(results['result']) > 0


def test_current_package_list_with_five_resources():
    results = libckan.logic.action.get.current_package_list_with_resources(
        limit=5)
    assert results['success'] is True
    assert len(results['result']) == 5






