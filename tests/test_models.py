__author__ = 'dgraziotin'

import nose.tools

from libckan.model import package
from libckan.model import serializable
from libckan.model import resource
from libckan.model import client
from libckan.model import exceptions
from libckan.model import trackingsummary


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


def test_resource():
    r = resource.Resource()
    assert r.created is None
    assert r.id == ''


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
