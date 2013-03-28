import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_organization_list():
    results = get.organization_list(client=client.Client(), order_by='',
        sort='', organizations='',
        all_fields='')
    assert results['success'] is True
    orgs = results['result']
    assert len(orgs) > 0
    assert orgs[0] != ''


def test_organization_list_for_user():
    results = get.organization_list_for_user(client=client.Client())
    assert results['success'] is True
    orgs = results['result']
    assert len(orgs) >= 0
    if len(orgs) > 0:
        assert orgs[0] != ''


def test_organization_show():
    results = get.organization_list(client=client.Client(), order_by='',
        sort='', organizations='',
        all_fields=True)
    assert results['success'] is True
    orgs = results['result']
    if len(orgs) > 0:
        results = get.organization_show(client=client.Client(),
            id=orgs[0]['id'])
        assert results['success'] is True
        assert results['result']['display_name'] == orgs[0]['display_name']
