from ruption import *
from util import VALUE, VALUE_TYPE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.is_none()
    a: Option[VALUE_TYPE] = ...
    a.is_none()
    none.is_none()
    none[VALUE_TYPE].is_none()
    some(VALUE).is_none()


def test_some_is_not_none():
    assert not some(VALUE).is_none()

def test_option_none_is_none():
    assert none.is_none()
