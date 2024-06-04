from imports import *


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.filter()
    a: Option[int] = ...
    a.filter()
    none().filter(lambda x: x > 0)
    none[int]().filter(lambda x: x > 0)
    some(1).filter()


# TODO write more obvious test
def test_filter():
    not_zero = lambda n: n!=0

    assert none().filter(not_zero).is_none()
    assert some(0).filter(not_zero).is_none()
    assert some(96).filter(not_zero).filter(lambda n: n == 96) == some(96)
    assert some(96).filter(not_zero).filter(lambda n: n > 101).is_none()
