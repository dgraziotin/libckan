import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exceptions


def test_vocabulary_list():
    results = get.vocabulary_list(client=client.Client())
    assert results['success'] is True
    assert isinstance(results['result'], list)


#TODO impossible to test for the moment
def test_term_translation_show():
    results = get.term_translation_show(client=client.Client(), terms='test')
    assert results['success'] is True
    assert isinstance(results['result'], list)


#TODO impossible to test for the moment
def test_vocabulary_show():
    return
    results = get.vocabulary_show(client=client.Client(), id='test')
    assert results['success'] is True


#TODO impossible to test for the moment
def test_format_autocomplete():
    results = get.format_autocomplete(client=client.Client(), q='test', limit='')
    assert results['success'] is True
    assert isinstance(results['result'], list)


