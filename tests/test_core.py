import pytest

from rust_option import Option

some, none = Option.some, Option.none

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
    next(iterator1)
    with pytest.raises(StopIteration):
        next(iterator1)

    iterator2 = some(12).iter()
    next(iterator2)
    with pytest.raises(StopIteration):
        next(iterator2)

def test_iter_on_some():
    iterator = some([1, 2 ,3]).iter()
    assert next(iterator) == [1, 2, 3]
