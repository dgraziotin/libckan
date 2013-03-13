import nose.tools
import libckan.logic.action.get
import libckan.model.exceptions


def test_site_read():
    results = libckan.logic.action.get.site_read()
    assert results['success'] is True
    assert results['result'] is True


def test_package_search_non_existing():
    results = libckan.logic.action.get.package_search(
        q='idonotexisth0pefllt123')
    assert results['success'] is True
    assert results['result']['count'] == 0
    assert results['result']['results'] == []


def test_package_search():
    results = libckan.logic.action.get.package_search(q='test')
    assert results['success'] is True
    assert results['result']['count'] > 0
    assert len(results['result']['results']) > 0


def test_package_list():
    results = libckan.logic.action.get.package_list()
    assert results['success'] is True
    assert len(results['result']) > 0
    assert isinstance(results['result'][0], unicode)


def test_current_package_list_with_resources():
    results = libckan.logic.action.get.current_package_list_with_resources()
    assert results['success'] is True
    assert len(results['result']) > 0


def test_current_package_list_with_five_resources():
    results = libckan.logic.action.get.current_package_list_with_resources(
        limit=5)
    assert results['success'] is True
    assert len(results['result']) == 5


def test_current_package_list_with_five_resources():
    results = libckan.logic.action.get.current_package_list_with_resources(
        limit=5)
    assert results['success'] is True
    assert len(results['result']) == 5
    assert results['result'][0]['name'] is not None
    assert isinstance(results['result'][0]['name'], unicode)


def test_revision_list():
    results = libckan.logic.action.get.revision_list()
    assert results['success'] is True
    assert len(results['result']) > 0
    assert isinstance(results['result'][0], unicode)


def test_package_revision_list():
    package = libckan.logic.action.get.package_search(q='test-bus-stops')
    if package['result']['count'] == 0:
        package = libckan.logic.action.get.package_search(q='test')
    package = package['result']['results'][0]
    results = libckan.logic.action.get.package_revision_list(id=package['id'])
    assert results['success'] is True
    print results
    assert len(results['result']) >= 0
    assert results['result'][0]['timestamp'] is not None


def test_related_list():
    package = libckan.logic.action.get.package_search(q='test-bus-stops')
    if package['result']['count'] == 0:
        package = libckan.logic.action.get.package_search(q='test')
    package = package['result']['results'][0]
    related = libckan.logic.action.get.related_list(id=package['id'])
    assert related['success'] is True
    if len(related['result']) > 0:
        assert related['result'][0]['view_count'] >= 0
        assert related['result'][0]['created'] != ''


def test_related_show():
    package_result = libckan.logic.action.get.package_search(q='test-bus-stops')
    if package_result['result']['count'] == 0:
        return

    package = package_result['result']['results'][0]
    related_to_package = libckan.logic.action.get.related_list(id=package['id'])

    assert related_to_package['success'] is True
    if len(related_to_package['result']) == 0:
        return

    related = related_to_package['result'][0]
    related_reget = libckan.logic.action.get.related_show(id=related['id'])
    related_reget = related_reget['result']
    # TODO see if there is a continuation to
    # http://lists.okfn.org/pipermail/ckan-dev/2013-March/004167.html
    assert related['id'] == related_reget['id']
    assert related['title'] == related_reget['title']


def test_group_list():
    groups = libckan.logic.action.get.group_list(all_fields=True)
    if len(groups['result']) == 0:
        return

    group = groups['result'][0]
    assert group['id'] is not None and group['id'] != u''
    assert isinstance(group['id'], unicode)


@nose.tools.raises(NotImplementedError)
def test_member_list():
    groups = libckan.logic.action.get.member_list(id='tobedone')


def test_organization_list():
    orgs = libckan.logic.action.get.organization_list(all_fields=True)
    if len(orgs['result']) == 0:
        return

    org = orgs['result'][0]
    assert org['id'] is not None and org['id'] != u''
    assert isinstance(org['id'], unicode)


def test_license_list():
    licenses = libckan.logic.action.get.licence_list()
    if len(licenses['result']) == 0:
        return

    found = False
    for lic in licenses['result']:
        assert lic['id'] is not None and lic['id'] != u''
        assert isinstance(lic['id'], unicode)
        if lic['title'].lower().find('open'):
            found = True

    if not found:
        print "No licenses found with 'open' term in them. Maybe not an error."
        assert True is False
