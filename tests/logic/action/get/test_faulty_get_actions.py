import nose.tools
import libckan.logic.action.get as get
import libckan.model.exceptions as exceptions


class Cl(object):
    def request(self, action, data):
        raise exceptions.CKANError('')
    def sanitize_params(self, params):
        raise exceptions.CKANError('')

#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_package_search_non_existing():
#    results = get.package_search(sort='213')
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_current_package_list_with_resources():
#    results = get.current_package_list_with_resources(
#        limit='hello')
#    assert results['success'] is True
#    assert len(results['result']) > 0
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_package_revision_list():
#    results = get.package_revision_list(id='sghegheghe213')
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_package_revision_list():
#    results = get.package_revision_list(id='idonotexisth0')
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_related_list():
#    get.related_list(id='raviouliraviouliformu')
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_related_show():
#    get.related_list(id=213)
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_group_list():
#    groups = get.group_list(sort='blah')
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_group_list2():
#    groups = get.group_list(groups=[123,432],all_fields=15)
#    print groups
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_organization_list():
#    groups = get.organization_list(sort='blah')
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_license_list():
#    fake_except = {'__type':'Fake Error', 'message': 'Fake Error'}
#    class Cl(object):
#        def request(self, action, data):
#            raise exceptions.CKANError(fake_except)
#        def sanitize_params(self, params):
#            raise exceptions.CKANError(fake_except)
#    licences = get.licence_list(client=Cl())
#
#
#@nose.tools.raises(exceptions.CKANError)
#def test_faulty_tag_list():
#    tags_str = get.tag_list()
#    tags_dicts = get.tag_list(vocabulary_id='blah')


@nose.tools.raises(exceptions.CKANError)
def test_package_autocomplete():
    results = get.package_autocomplete(q=666)


@nose.tools.raises(exceptions.CKANError)
def test_package_list():
    results = get.package_list(client=Cl())


@nose.tools.raises(exceptions.CKANError)
def test_package_relationships_list():
    results = get.package_relationships_list(id=666,
        id2=777, rel=876)


@nose.tools.raises(exceptions.CKANError)
def test_faulty_package_search():
    results = get.package_search(q=666, fq='',
        rows='', sort='', start='', qf='', facet='',
        facet_mincount='', facet_limit='',
        facet_field='', count='', results='',
        facets='', search_facets='')
    assert results['success'] is True
    assert isinstance(results['result']['results'], list)
    assert len(results['result']['results']) > 0
    results['result']['results'][0]['name'] != ''


@nose.tools.raises(exceptions.CKANError)
def test_package_show():
    results = get.package_show(id='fewKo43rokg34ov,ro,fowng2oiw')


@nose.tools.raises(exceptions.CKANError)
def test_current_package_list_with_resources():
    results = get.current_package_list_with_resources(limit='a',
        page='b')
    assert results['success'] is True
    assert len(results['result']) > 0
    assert results['result'][0] != ''


@nose.tools.raises(exceptions.CKANError)
def test_group_package_show():
    results = get.group_package_show(id=666)


@nose.tools.raises(exceptions.CKANError)
def test_group_list():
    results = get.group_list(order_by=666,
        sort='',
        groups='', all_fields='')


@nose.tools.raises(exceptions.CKANError)
def test_group_list_authz():
    results = get.group_list_authz(client=Cl(), available_only=-15)


@nose.tools.raises(exceptions.CKANError)
def test_group_show():
    groups = get.group_list(order_by=666,
        sort=666,
        groups='', all_fields='')
    group = groups['result'][0]
    results = get.group_show(id=group)
    assert results['success'] is True
    assert results['result']['display_name'].lower() == group.lower()


@nose.tools.raises(exceptions.CKANError)
def test_tag_list():
    results = get.tag_list(query=123, vocabulary_id=987, all_fields=True)
    tags = results['result']
    assert results['success'] is True
    assert len(tags) > 0
    assert isinstance(tags[0], dict)
    assert tags[0]['display_name'] != ''


@nose.tools.raises(exceptions.CKANError)
def test_tag_autocomplete():
    results = get.tag_list(query='raviuoliraviuoligivemethepotiuoli',
        vocabulary_id=-123, all_fields=False)
    tags = results['result']


@nose.tools.raises(exceptions.CKANError)
def test_tag_search():
    results = get.tag_list(query='raviuoliraviuoligivemethepotiuoli',
        vocabulary_id=-123, all_fields=False)


@nose.tools.raises(exceptions.CKANError)
def test_tag_show():
    results = get.tag_show(id='lkj')

