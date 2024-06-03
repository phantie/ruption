from ruption import *
from util import VALUE, VALUE_TYPE, OTHER_VALUE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.contains(VALUE)
    a: Option[VALUE_TYPE] = ...
    a.contains(VALUE)
    none().contains(VALUE)
    none[int]().contains(VALUE)
    some(VALUE).contains(VALUE)


def test_some_value_contains_value():
    assert some(VALUE).contains(VALUE)

def test_some_value_does_not_contain_other_value():
    assert not some(VALUE).contains(OTHER_VALUE)

def test_none_does_not_contain_value():
    assert not none().contains(VALUE)