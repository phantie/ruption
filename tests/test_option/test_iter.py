from ruption import *
from util import VALUE, VALUE_TYPE, OTHER_VALUE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.iter()
    a: Option[VALUE_TYPE] = ...
    a.iter()
    none().iter()
    none[int]().iter()
    some(VALUE).iter()


def test_iter_some():
    assert list(some(VALUE).iter()) == [VALUE]

def test_iter_none():
    assert list(none().iter()) == []
