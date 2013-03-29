import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_user_list():
    results = get.user_list(client=client.Client(), q='', order_by='')
    assert results['success'] is True
    assert len(results['result']) > 0
    assert isinstance(results['result'][0], dict)
    assert results['result'][0]['name'] != ''


def test_user_autocomplete():
    results = get.user_list(client=client.Client(), q='', order_by='')
    assert results['success'] is True
    assert len(results['result']) > 0
    assert isinstance(results['result'][0], dict)
    name = results['result'][0]['name']
    assert name != ''
    results = get.user_autocomplete(client=client.Client(), q=name[:3])
    assert results['success'] is True
    found = False
    for result in results['result']:
        if result['name'] == name:
            found = True
    assert found == True


def test_user_show():
    results = get.user_list(client=client.Client(), q='', order_by='')
    assert results['success'] is True
    assert len(results['result']) > 0
    assert isinstance(results['result'][0], dict)
    id = results['result'][0]['id']
    name = results['result'][0]['name']
    results = get.user_show(client=client.Client(), id=id)
    assert results['result']['id'] == id
    assert results['result']['name'] == name


def test_member_list():
    groups = get.group_list(client=client.Client(), order_by='',
        sort='', groups='', all_fields='')
    group = groups['result'][0]
    results = get.member_list(client=client.Client(), id=group)
    print results['result']
    assert results['success'] is True
    assert len(results['result']) > 0



