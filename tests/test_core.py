import pytest

from rust_option import Option, some, none

def test_option_none_raises_option_ValueIsNone_if_unwrap():
    with pytest.raises(Option.ValueIsNone):
        none.unwrap()

def test_unwrap_of_some_number_returns_the_number():
    assert some(42).unwrap() == 42

def test_some_is_not_none():
    assert not some('one').is_none()

def test_option_none_is_equal_to_None():
    assert none == None

def test_option_none_equals_to_self():
    assert none == none

def test_unwrap_or_returns_other_if_target_is_option_none():
    other = "Me called other, other is not this."
    assert none.unwrap_or(other) == other

def test_converts_python_None_into_option_none():
    assert Option.into(None) is none

def test_option_into_returns_option_some_if_arg_is_not_None():
    assert isinstance(Option.into(13), Option.some)

def test_converts_not_None_into_option_some():
    some_value = "Me not none, me some."
    assert Option.into(some_value) == some(some_value)

def test_some_13_not_equals_some_42():
    assert some(13) != some(42)

def test_option_some_is_what_it_is():
    assert some(0).is_some()

def test_option_none_is_what_it_is():
    assert none.is_none()

def test_unwrap_or_else_executes_function_on_option_none():
    assert none.unwrap_or_else(lambda: 42) == 42

def test_map_on_none_returns_self():
    assert none.map(lambda x: x**2) == none

def test_map_on_some_transforms_some():
    assert some(6).map(lambda x: x**2) == some(36)

def test_map_or_on_none_returns_else():
    assert none.map_or(33, lambda x: x**2) == 33

def test_map_or_else_on_none_returns_result_of_default_func():
    assert none.map_or_else(lambda: 42, lambda: 13) == 42

def test_map_or_else_on_none_executes_function_that_changes_state():
    def change_state_of_local_var():
        nonlocal local
        local += 6
        
    local = 14

    none.map_or_else(change_state_of_local_var, lambda: None)
    assert local == 20

def test_raises_StopIteration_after_executing_next_twice():
    iterator1 = none.iter()
    assert next(iterator1) is none
    with pytest.raises(StopIteration):
        next(iterator1)

    iterator2 = some(12).iter()
    assert next(iterator2) == 12
    with pytest.raises(StopIteration):
        next(iterator2)

def test_iter_on_some():
    iterator = some([1, 2 ,3]).iter()
    assert next(iterator) == [1, 2, 3]

def test_and_then():
    square = lambda x: x**2

    assert some(2).and_then(square).and_then(square) == some(16)
    assert some(13).and_then(lambda self: none) is none
    assert some(33).and_then(lambda self: none).and_then(square) is none
    assert none.and_then(lambda x: x**2) is none

def test_filter():
    not_zero = lambda n: n!=0

    assert none.filter(not_zero) is none
    assert some(0).filter(not_zero) is none
    assert some(96).filter(not_zero).filter(lambda n: n == 96) == some(96)
    assert some(96).filter(not_zero).filter(lambda n: n > 101) is none

def test_otherwise():
    a, b = some(3), none

    assert a.otherwise(b) == a
    assert b.otherwise(a) == a
    assert a.otherwise(some(4)) == a
    assert b.otherwise(b) is b

def test_or_else():
    nobody = lambda: none
    vikings = lambda: some('vikings')

    assert some('barbarians').or_else(vikings) == some('barbarians')
    assert none.or_else(vikings) == some('vikings')
    assert none.or_else(nobody) is none

def test_xor():
    x, y = some(2), none
    assert x.xor(y) == some(2)

    x, y = none, some(2)
    assert x.xor(y) == some(2)

    x = y = some(2)
    assert x.xor(y) is none

    x = y = none
    assert x.xor(y) is none