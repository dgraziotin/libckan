import nose.tools
import libckan.model.exceptions as exceptions

@nose.tools.raises(exceptions.CKANError)
def test_ckanerror():
    try:
        raise exceptions.CKANError({'message':'this is a test', '__type':'A custom type'})
    except exceptions.CKANError as e:
        print e
        print e.__repr__
    raise exceptions.CKANError({'message':'this is a test', '__type':'A custom type'})
