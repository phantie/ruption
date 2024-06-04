from imports import *


def test_and_():
    x = some(VALUE)
    y = none()

    assert x.and_(y).is_none()
    assert y.and_(x).is_none()

    x = some(VALUE)
    y = some(OTHER_VALUE)

    assert x.and_(y) == y
    assert y.and_(x) == x

    x = y = none()

    assert x.and_(y).is_none()