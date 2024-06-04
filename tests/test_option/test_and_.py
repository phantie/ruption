from ruption import *
from util import VALUE, OTHER_VALUE


def test_and_():
    x = some(VALUE)
    y = none()

    assert x.and_(y).is_none()
    assert y.and_(x).is_none()

    x = some(VALUE)
    y = some(OTHER_VALUE)

    assert x.and_(y) == some(OTHER_VALUE)
    assert y.and_(x) == some(VALUE)

    x = y = none()

    assert x.and_(y).is_none()