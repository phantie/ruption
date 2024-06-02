from ruption import *
from util import VALUE, VALUE_TYPE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.is_some()
    a: Option[VALUE_TYPE] = ...
    a.is_some()
    none.is_some()
    none[VALUE_TYPE].is_some()
    some(VALUE).is_some()


def test_some_is_some():
    assert some(VALUE).is_some()

def test_none_is_not_some():
    assert not none.is_some()
