from ruption.pacify import pacify_callable_result
from numbers import Number


@pacify_callable_result()
def divide(dividend: Number, divisor: Number) -> Number:
    return dividend / divisor

def test_pacify_callable_result_exception():
    assert isinstance(divide(1, 0).unwrap_err(), ZeroDivisionError)

def test_pacify_callable_result_success():
    assert divide(10, 5).unwrap() == 2


