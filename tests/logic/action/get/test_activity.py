import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


@nose.tools.raises(exceptions.CKANError)
def test_dashboard_activity_list():
    results = get.dashboard_activity_list(client=client.Client(),
            offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_dashboard_activity_list_html():
    results = get.dashboard_activity_list_html(client=client.Client(),
            offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_dashboard_new_activities_count():
    results = get.dashboard_new_activities_count(client=client.Client())
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_activity_detail_list():
    results = get.activity_detail_list(client=client.Client(), id='')
    assert results['success'] is True



@nose.tools.raises(exceptions.CKANError)
def test_group_activity_list():
    results = get.group_activity_list(client=client.Client(), id='', offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_group_activity_list_html():
    results = get.group_activity_list_html(client=client.Client(), id='', offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_organization_activity_list():
    results = get.organization_activity_list(client=client.Client(), id='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_organization_activity_list_html():
    results = get.organization_activity_list_html(client=client.Client(), id='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_package_activity_list():
    results = get.package_activity_list(client=client.Client(), id='', offset='', limit='')
    assert results['success'] is True



@nose.tools.raises(exceptions.CKANError)
def test_package_activity_list_html():
    results = get.package_activity_list_html(client=client.Client(), id='', offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_user_activity_list():
    results = get.user_activity_list(client=client.Client(), id='', offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_user_activity_list_html():
    results = get.user_activity_list_html(client=client.Client(), id='', offset='', limit='')
    assert results['success'] is True


def test_recently_changed_packages_activity_list():
    results = get.recently_changed_packages_activity_list(client=client.Client(), offset='', limit='')
    assert results['success'] is True


@nose.tools.raises(exceptions.CKANError)
def test_recently_changed_packages_activity_list_html():
    results = get.recently_changed_packages_activity_list_html(client=client.Client(), offset='', limit='')
    assert results['success'] is True



