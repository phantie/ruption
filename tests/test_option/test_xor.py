from ruption import *
from util import VALUE, OTHER_VALUE


def test_xor():
    x = some(VALUE)
    y = none()

    assert x.xor(y) == x
    assert y.xor(x) == x

    x = some(VALUE)
    y = some(OTHER_VALUE)

    assert x.xor(y).is_none()
    assert y.xor(x).is_none()

    x = y = none()

    assert x.xor(y).is_none()