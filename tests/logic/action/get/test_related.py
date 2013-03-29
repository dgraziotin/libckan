import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_related_list():
    packages = get.package_list(client=client.Client())
    assert len(packages['result']) > 0
    import random
    pkg = random.choice(packages['result'])
    results = get.related_list(client=client.Client(), id=pkg)
    assert results['success'] is True
    assert isinstance(results['result'], list)


def test_related_show():
    packages = get.package_list(client=client.Client())
    assert len(packages['result']) > 0
    import random
    pkg = random.choice(packages['result'])
    results = get.related_list(client=client.Client(), id=pkg)
    assert results['success'] is True
    assert isinstance(results['result'], list)
    if len(results['result']) > 0:
        results = get.related_show(id=results['result'][0]['id'])
        assert results['success'] is True



