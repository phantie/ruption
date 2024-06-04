from ruption.pacify import pacify_callable_result
from ruption.result import err, ok
from numbers import Number


@pacify_callable_result()
def divide(dividend: Number, divisor: Number) -> Number:
    return dividend / divisor

# TODO tweak test when is_err, unwrap_err are available
def test_pacify_callable_result_exception():
    r = divide(1, 0)
    assert isinstance(r, err)
    assert isinstance(r.T, ZeroDivisionError)

# TODO tweak test when is_ok are available
def test_pacify_callable_result_success():
    r = divide(10, 5)
    assert isinstance(r, ok)
    assert r.unwrap() == 2


