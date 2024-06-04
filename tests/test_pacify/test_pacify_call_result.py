from ruption.pacify import pacify_call_result

def test_pacify_call_exception():
    assert isinstance(pacify_call_result(lambda: 1/0).unwrap_err(), ZeroDivisionError)

def test_pacify_call_success():
    VALUE = 100
    assert pacify_call_result(lambda: VALUE).unwrap() == VALUE