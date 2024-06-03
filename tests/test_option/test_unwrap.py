from ruption import *
from util import VALUE, VALUE_TYPE


def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    def _():
        a: Option = ...
        a.unwrap()
    a: Option[VALUE_TYPE] = ...
    a.unwrap()
    lambda: none().unwrap()
    lambda: none[VALUE_TYPE]().unwrap()
    some(VALUE).unwrap()

def test_option_none_raises_option_noneValue_if_unwrap():
    import pytest
    with pytest.raises(Panic) as err:
        none().unwrap()

    assert str(err.value) == 'called `Option.unwrap()` on a `none` value'


def test_unwrap_of_some_value_returns_the_value():
    assert some(VALUE).unwrap() == VALUE
