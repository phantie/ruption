from ruption import *
from util import VALUE, VALUE_TYPE, OTHER_VALUE, OTHER_TYPE, OTHER_TYPE_VALUE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    
    def _():
        a: Option = ...
        a.map(lambda value: VALUE)
    a: Option[VALUE_TYPE] = ...
    a.map(lambda value: VALUE)
    none().map(lambda value: VALUE)
    none[int]().map(lambda value: VALUE)

    # check filter
    some(VALUE).map(map_value_to_other_type_value).filter()


def map_value_to_other_type_value(value: VALUE_TYPE) -> OTHER_TYPE:
    return OTHER_TYPE_VALUE

def test_map_some_value_to_other_type_value():
    assert some(VALUE).map(map_value_to_other_type_value).contains(OTHER_TYPE_VALUE)

def test_map_none():
    assert none().map(map_value_to_other_type_value).is_none()
