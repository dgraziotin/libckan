__author__ = 'dgraziotin'

import nose.tools

from libckan.model import package
from libckan.model import serializable
from libckan.model import resource
from libckan.model import client
from libckan.model import exceptions
from libckan.model import trackingsummary
from libckan.model import tag
from libckan.model import extra


@nose.tools.raises(NotImplementedError)
def test_serializable_init():
    s = serializable.Serializable()


@nose.tools.raises(NotImplementedError)
def test_serializable_from_dict():
    serializable.Serializable.from_dict({})


@nose.tools.raises(NotImplementedError)
def test_serializable_to_dict():
    serializable.Serializable.to_dict()


def test_package_init():
    p = package.Package()
    assert p.name == ''
    assert p.type is None
    assert p.extras == []
    assert isinstance(p.tracking_summary, trackingsummary.TrackingSummary)
    assert p.tracking_summary.recent == 0 and p.tracking_summary.total == 0
    assert p.tags == []


def test_tags():
    p = package.Package()
    assert p.tags == []
    assert p.num_tags == 0
    tag_obj = tag.Tag()
    tag_obj.display_name = 'tag 1'
    tag_obj.state = 'active'
    p.add_tag(tag_obj)
    assert p.num_tags == 1
    assert p.tags[0] == tag_obj


def test_extras():
    p = package.Package()
    extra_obj = extra.Extra()
    assert extra_obj.id == '' and extra_obj.revision_timestamp == ''
    extra_obj.id = 'fakeid123'
    extra_obj.key = 'fakekey'
    extra_obj.value = 'fakevalue'
    p.add_extra(extra_obj)
    assert len(p.extras) == 1
    assert p.extras[0] == extra_obj



def test_resource():
    r = resource.Resource()
    assert r.created is None
    assert r.id == ''


@nose.tools.raises(ValueError)
def test_add_wrong_resource():
    p = package.Package()
    p.add_resource(tag.Tag())


@nose.tools.raises(ValueError)
def test_add_wrong_tag():
    p = package.Package()
    p.add_tag(resource.Resource())


@nose.tools.raises(ValueError)
def test_add_wrong_extra():
    p = package.Package()
    p.add_extra('haaaai')


@nose.tools.raises(ValueError)
def test_from_dict_wrong_data():
    serializable.Serializable.from_dict('hellooo')


@nose.tools.raises(ValueError)
def test_package_from_dict_wrong_data():
    p = package.Package.from_dict(123)


def test_response_init():
    r = client.Response()
    assert r.help == None
    assert r.result == None
    assert r.success == None

@nose.tools.raises(exceptions.CKANError)
def test_ckanerror():
    try:
        raise exceptions.CKANError({'message':'this is a test', '__type':'A custom type'})
    except exceptions.CKANError as e:
        print e
        print e.__repr__
    raise exceptions.CKANError({'message':'this is a test', '__type':'A custom type'})
