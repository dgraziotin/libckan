import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_group_list():
    results = get.group_list(client=client.Client(), order_by='',
        sort='',
        groups='', all_fields='')
    assert results['success'] is True
    assert len(results['result']) > 0
    assert results['result'][0] != ''
    results = get.group_list(client=client.Client(),  all_fields=True)
    assert results['success'] is True
    assert len(results['result']) > 0
    assert isinstance(results['result'][0], dict)


def test_group_list_authz():
    results = get.group_list_authz(client=client.Client(), available_only='')
    assert results['success'] is True
    assert len(results['result']) >= 0


def test_group_show():
    groups = get.group_list(client=client.Client(), order_by='',
        sort='',
        groups='', all_fields='')
    group = groups['result'][0]
    results = get.group_show(client=client.Client(), id=group)
    assert results['success'] is True
    assert results['result']['display_name'].lower() == group.lower()


