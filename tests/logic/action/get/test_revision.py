import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_revision_list():
    results = get.revision_list(client=client.Client())
    assert results['success'] is True
    if len(results['result']) > 0:
        assert results['result'][0] != ''


def test_revision_show():
    results = get.revision_list(client=client.Client())
    assert results['success'] is True
    if len(results['result']) > 0:
        assert results['result'][0] != ''
        results = get.revision_show(client=client.Client(),
            id=results['result'][0])
        assert results['success'] is True
        assert results['result']['timestamp'] != ''


def test_package_revision_list():
    results = get.package_search(q='test')
    assert results['success'] is True
    assert results['result']['count'] > 0
    pkg = results['result']['results'][0]
    revs = get.package_revision_list(client=client.Client(), id=pkg['id'])
    assert revs['success'] is True
    assert revs['result'][0]['timestamp'] != ''


def test_group_revision_list():
    groups = get.group_list()
    assert groups['success'] == True
    group = groups['result'][0]
    results = get.group_revision_list(client=client.Client(), id=group)
    assert results['success'] is True
    assert results['result'][0]['timestamp'] != ''



