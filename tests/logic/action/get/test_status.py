import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_status_show():
    results = get.status_show(client=client.Client())
    assert results['success'] is True
    assert results['result']['site_url'] == client.Client()._base_url


def test_resource_status_show():
    results = get.resource_search(client=client.Client(),
        query='name:bus-stops')
    assert results['success'] is True
    if results['result']['count'] > 0:
        id = results['result']['results'][0]['id']
        results = get.resource_status_show(client=client.Client(), id=id)
        assert results['success'] is True


def test_task_status_show():
    results = get.resource_search(client=client.Client(),
        query='name:bus-stops')
    assert results['success'] is True
    if results['result']['count'] > 0:
        id = results['result']['results'][0]['id']
        results = get.resource_status_show(client=client.Client(), id=id)
        assert results['success'] is True
        if results['result']['message']:
            return
        results = get.task_status_show(client=client.Client(), entity_id=id)
        assert results['success'] is True



