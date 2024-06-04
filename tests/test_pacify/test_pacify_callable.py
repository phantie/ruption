from ruption.pacify import pacify_callable
from numbers import Number


@pacify_callable(log = False)
def divide(dividend: Number, divisor: Number) -> Number:
    return dividend / divisor

def test_pacify_callable_exception():
    assert divide(1, 0).is_none()

def test_pacify_callable_success():
    assert divide(10, 5).contains(2)


