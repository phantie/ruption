from imports import *


def test_or_():
    x = some(VALUE)
    y = none()

    assert x.or_(y) == x
    assert y.or_(x) == x

    x = some(VALUE)
    y = some(OTHER_VALUE)

    assert x.or_(y) == x
    assert y.or_(x) == y

    x = y = none()

    assert x.or_(y).is_none()