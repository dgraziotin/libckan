import nose.tools
import libckan.logic.action.get as get
import libckan.model.client as client
import libckan.model.exceptions as exception


def test_tag_list():
    results = get.tag_list(query='', vocabulary_id='', all_fields=False)
    tags = results['result']
    assert results['success'] is True
    assert len(tags) > 0
    assert tags[0] != ''

    results = get.tag_list(query='', vocabulary_id='', all_fields=True)
    tags = results['result']
    assert results['success'] is True
    assert len(tags) > 0
    assert isinstance(tags[0], dict)
    assert tags[0]['display_name'] != ''


def test_tag_autocomplete():
    results = get.tag_list(query='', vocabulary_id='', all_fields=False)
    tags = results['result']
    tag = tags[0]
    tag_len = len(tag)
    offset = tag_len - 4 if tag_len >= 5 else 1
    results = get.tag_autocomplete(client=client.Client(), query=tag[:offset])
    assert results['success'] is True
    assert len(results['result']) >= 0
    assert tag in results['result']


def test_tag_search():
    results = get.tag_list(query='', vocabulary_id='', all_fields=False)
    tags = results['result']
    tag = tags[0]

    results = get.tag_search(client=client.Client(), query=tag)
    print results['result']
    assert results['success'] is True
    assert len(results['result']['results']) >= 0
    found = False
    for result in results['result']['results']:
        if result['name'] == tag:
            found = True
    assert found == True


def test_tag_show():
    results = get.tag_list(query='', vocabulary_id='', all_fields=False)
    tags = results['result']
    tag = tags[0]
    results = get.tag_show(client=client.Client(), id=tag)
    assert results['success'] is True
    assert results['result']['display_name'] == tag



