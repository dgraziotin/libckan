import nose.tools
import libckan.logic.action.get
import libckan.model.exceptions as exceptions

@nose.tools.raises(exceptions.CKANError)
def test_faulty_package_search_non_existing():
    results = libckan.logic.action.get.package_search(sort='213')


@nose.tools.raises(exceptions.CKANError)
def test_faulty_current_package_list_with_resources():
    results = libckan.logic.action.get.current_package_list_with_resources(
        limit='hello')
    assert results['success'] is True
    assert len(results['result']) > 0


@nose.tools.raises(exceptions.CKANError)
def test_faulty_package_revision_list():
    results = libckan.logic.action.get.package_revision_list(id='sghegheghe213')


@nose.tools.raises(libckan.model.exceptions.CKANError)
def test_faulty_package_revision_list():
    results = libckan.logic.action.get.package_revision_list(id='idonotexisth0')


@nose.tools.raises(exceptions.CKANError)
def test_faulty_related_list():
    libckan.logic.action.get.related_list(id='raviouliraviouliformu')


@nose.tools.raises(exceptions.CKANError)
def test_faulty_related_show():
    libckan.logic.action.get.related_list(id=213)


@nose.tools.raises(exceptions.CKANError)
def test_faulty_group_list():
    groups = libckan.logic.action.get.group_list(sort='blah')


@nose.tools.raises(exceptions.CKANError)
def test_faulty_group_list2():
    groups = libckan.logic.action.get.group_list(groups=[123,432],all_fields=15)
    print groups


@nose.tools.raises(exceptions.CKANError)
def test_faulty_organization_list():
    groups = libckan.logic.action.get.organization_list(sort='blah')


@nose.tools.raises(exceptions.CKANError)
def test_faulty_license_list():
    fake_except = {'__type':'Fake Error', 'message': 'Fake Error'}
    class Cl(object):
        def request(self, action, data):
            raise exceptions.CKANError(fake_except)
    licences = libckan.logic.action.get.licence_list(client=Cl())