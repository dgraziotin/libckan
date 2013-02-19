__author__ = 'dgraziotin'

import nose.tools

from libckan.model import package
from libckan.model import resource
from libckan.model import serializable


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
    assert p.type == None
    assert p.extras == None