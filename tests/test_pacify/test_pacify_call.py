from ruption.pacify import pacify_call

def test_pacify_call_exception():
    assert pacify_call(lambda: 1/0, log = False).is_none()

def test_pacify_call_success():
    VALUE = 100
    assert pacify_call(lambda: VALUE, log = False).contains(VALUE)