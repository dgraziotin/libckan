import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_resource_search():
    results = get.resource_search(client=client.Client(), query='name:csv')
    assert results['success'] is True
    if results['result']['count'] > 0:
        print results['result']['results']
        assert isinstance(results['result']['results'][0], dict)
        assert results['result']['results'][0]['name'] != ''


def test_resource_show():
    results = get.resource_search(client=client.Client(), query='name:csv')
    assert results['success'] is True
    if results['result']['count'] > 0:
        res_orig = results['result']['results'][0]
        try:
            res_show = get.resource_show(client=client.Client(), id=res_orig['id'])
            assert results['success'] is True
            assert res_show['id'] == res_orig['id']
        except exceptions.CKANError, e:
            if str(e.type).lower().find('auth') >= 0:
                return
            else:
                raise exceptions.CKANError(e)



