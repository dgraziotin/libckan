import nose
import libckan.model.client as client


def test__sanitize():
    params = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    results = client.Client.sanitize_params(params)
    assert results == params


@nose.tools.raises(TypeError)
def test__sanitize_nonvalid():
    results = client.Client.sanitize_params('')