from ruption.pacify import pacify_call_result
from ruption.result import ok, err

# TODO tweak test when is_err and unwrap_err are available
def test_pacify_call_exception():
    r = pacify_call_result(lambda: 1/0)
    assert isinstance(r, err)
    assert isinstance(r.T, ZeroDivisionError)

# TODO tweak test when is_ok are available
def test_pacify_call_success():
    VALUE = 100
    r = pacify_call_result(lambda: VALUE)
    assert isinstance(r, ok)
    assert r.unwrap() == VALUE