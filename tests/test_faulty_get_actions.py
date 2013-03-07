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