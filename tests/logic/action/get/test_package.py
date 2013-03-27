import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_package_autocomplete():
    results = get.package_autocomplete(client=client.Client(), q='test')
    assert results['success'] is True
    print results
    assert isinstance(results['result'],list)
    if len(results['result']) > 0:
        assert results['result'][0]['match_field'] != ''


def test_package_list():
    results = get.package_list(client=client.Client())
    assert results['success'] is True
    assert len(results['result']) > 0
    assert results['result'][0] != ''


def test_package_relationships_list():
    results = get.package_relationships_list(client=client.Client(), id='test',
        id2='test', rel='')
    print results
    assert results['success'] is True
    assert results['result'] == []


def test_package_search():
    results = get.package_search(client=client.Client(), q='test', fq='',
        rows='', sort='', start='', qf='', facet='',
        facet_mincount='', facet_limit='',
        facet_field='', count='', results='',
        facets='', search_facets='')
    assert results['success'] is True
    assert isinstance(results['result']['results'], list)
    assert len(results['result']['results']) > 0
    results['result']['results'][0]['name'] != ''


def test_package_show():
    results = get.package_show(client=client.Client(), id='test')
    assert results['success'] is True
    assert isinstance(results['result'], dict)
    assert results['result']['name'] == 'test'


def test_current_package_list_with_resources():
    results = get.current_package_list_with_resources(client=client.Client(),
        limit='',
        page='')
    assert results['success'] is True
    assert len(results['result']) > 0
    assert results['result'][0] != ''


def test_group_package_show():
    groups = get.group_list(client=client.Client())
    assert groups['success'] is True
    group = groups['result'][0]
    results = get.group_package_show(client=client.Client(), id=group)
    assert results['success'] is True
    assert len(results['result']) > 0
    assert results['result'][0]['name'] != ''




