from ruption import *
from util import VALUE, OTHER_VALUE


def test_option_none_not_equal_to_None():
    assert none() != None

def test_option_none_equals_to_self():
    assert none() == none()

def test_some_value_not_eq_to_other_value():
    assert some(VALUE) != some(OTHER_VALUE)
