import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_licence_list():
    results = get.licence_list(client=client.Client())
    print results['result']
    assert results['success'] is True
    assert isinstance(results['result'], list)
    import random
    lic = random.choice(results['result'])
    assert isinstance(lic, dict)
    assert lic['title'] != ''


def test_site_read():
    results = get.site_read(client=client.Client())
    assert results['success'] is True
    assert results['result'] is True



