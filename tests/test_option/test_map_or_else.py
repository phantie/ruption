from ruption import *
from util import VALUE, VALUE_TYPE, OTHER_VALUE, OTHER_TYPE, OTHER_TYPE_VALUE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    
    def _():
        a: Option = ...
        a.map_or_else(lambda: VALUE, lambda value: VALUE)
    a: Option[VALUE_TYPE] = ...
    a.map_or_else(lambda: VALUE, lambda value: VALUE)
    none().map_or_else(lambda: VALUE, lambda value: VALUE)
    none[int]().map_or_else(lambda: VALUE, lambda value: VALUE)

    # check filter
    some(VALUE).map_or_else(lambda: OTHER_TYPE_VALUE, map_value_to_other_type_value).filter()


def map_value_to_other_type_value(value: VALUE_TYPE) -> OTHER_TYPE:
    return OTHER_TYPE_VALUE

def test_map_or_some_value_to_other_type_value():
    assert some(VALUE).map_or_else(..., map_value_to_other_type_value).contains(OTHER_TYPE_VALUE)

def test_map_or_else_none():
    assert none().map_or_else(lambda: OTHER_TYPE_VALUE, ...).contains(OTHER_TYPE_VALUE)
