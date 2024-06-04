from imports import *


def test_some_ok_or():
    assert some(VALUE).ok_or(OTHER_VALUE) == ok(VALUE)

def test_none_ok_or():
    assert none().ok_or(OTHER_VALUE) == err(OTHER_VALUE)