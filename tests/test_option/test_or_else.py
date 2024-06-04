from imports import *


def test_or_else():
    nobody = lambda: none()
    vikings = lambda: some(VALUE)

    assert some(OTHER_VALUE).or_else(vikings) == some(OTHER_VALUE)
    assert none().or_else(vikings) == some(VALUE)
    assert none().or_else(nobody).is_none()
