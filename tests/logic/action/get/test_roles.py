import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_member_roles_list():
    results = get.member_roles_list(client=client.Client())
    assert results['success'] is True
    assert isinstance(results['result'][0], dict)


def test_roles_show():
    results = get.package_search(client=client.Client(), q='test')
    assert results['success'] is True
    id = results['result']['results'][0]['id']
    results = get.roles_show(client=client.Client(), domain_object=id)
    print results['result']
    assert results['success'] is True
    assert results['result']['domain_object_type'] == 'Package'
    assert isinstance(results['result']['roles'], list)



