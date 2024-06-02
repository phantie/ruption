from ruption import *
from util import VALUE, VALUE_TYPE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.unwrap_or(VALUE)
    a: Option[VALUE_TYPE] = ...
    a.unwrap_or(VALUE)
    none.unwrap_or(VALUE)
    none[VALUE_TYPE].unwrap_or(VALUE)
    some(VALUE).unwrap_or(VALUE)




def test_unwrap_or_returns_default_if_called_on_none():
    assert none.unwrap_or(VALUE) == VALUE
