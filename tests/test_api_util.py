import nose
import libckan.logic.action.get as get


def test__sanitize():
    params = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    results = get._sanitize(params)
    assert results == params


@nose.tools.raises(TypeError)
def test__sanitize_nonvalid():
    results = get._sanitize('')