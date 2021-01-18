import pytest

from ruption import *

def test_option_none_raises_option_noneValue_if_unwrap():
    with pytest.raises(Panic) as err:
        none.unwrap()

    assert str(err.value) == 'called `Option.unwrap()` on a `none` value'

def test_unwrap_of_some_variable_returns_the_variable():
    assert some(42).unwrap() == 42

def test_some_is_not_none():
    assert not some('one').is_none()

def test_option_none_not_equal_to_None():
    assert none != None

def test_option_none_equals_to_self():
    assert none == none

def test_unwrap_or_returns_other_if_target_is_option_none():
    other = "Me called other, other is not this."
    assert none.unwrap_or(other) == other

def test_converts_python_None_into_option_none():
    assert Option.into(None) is none

def test_option_into_returns_option_some_if_arg_is_not_None():
    assert isinstance(Option.into(13), some)

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

def test__or():
    a, b = some(3), none

    assert a._or(b) == a
    assert b._or(a) == a
    assert a._or(some(4)) == a
    assert b._or(b) is b

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


def test_zip():
    x = some(1)
    y = some('hey')
    z = none

    assert x.zip(y) == some((1, 'hey'))
    assert x.zip(z) is none
    assert z.zip(z) is none

def test_zip_advanced():
    x = some(1)
    y = some('hey')
    z = none

    assert x.zip(y, z, x) is none
    assert x.zip(y, y) == some((1, 'hey', 'hey'))
    assert x.zip(x, x, x, x) == some((1, 1, 1, 1, 1))

    with pytest.raises(TypeError):
        x.zip() == some((1,))

def test_zip_with():
    def area(a, b):
        return a*b

    x = some(10)
    y = some(15)
    z = some(5)

    assert x.zip_with(y, f = area) == some(150)
    assert x.zip_with(y, z, f = lambda x, y, z: x - y + z ) == some(0)
    assert x.zip_with(none, x, f = area) is none

    assert none.zip_with(y, y, f = area) is none

    with pytest.raises(TypeError):
        x.zip_with()

def test_copied():
    x = some('num')
    y = x.copied()
    assert not x is y

    # there`s no point in actual copy of none. so it`s ommitted.
    assert none.copied() is none


def test_expect_none():
    with pytest.raises(Panic):
        some(1).expect_none()

    assert none.expect_none() is None

def test_unwrap_none():
    with pytest.raises(Panic):
        some(1).unwrap_none()

    assert none.unwrap_none() is none

def test_unwrap_or_default():
    assert some(1).unwrap_or_default(int) == 1
    assert none.unwrap_or_default(int) == 0
    assert none.unwrap_or_default(list) == []

def test_flatten():
    assert some(1) == some(some(1)).flatten()
    assert 1 == some(some(1)).flatten().flatten()
    assert some(1) == some(some(some(1))).flatten().flatten()
    assert none is some(none).flatten()
    assert none is none.flatten()

    assert 1 == some(some(1)).flatten(2)
    assert some(1) == some(some(some(1))).flatten(2)
    assert none is some(none).flatten(13)
    assert none is none.flatten(13)


def test_also():
    x = some(2)
    y = none

    assert x.also(y) is none

    x = none
    y = some('foo')

    assert x.also(y) is none

    x = some(2)
    y = some(3)

    assert x.also(y) == some(3)

    x = y = none

    assert x.also(y) is none

def test__and():
    x = some(2)
    y = none

    assert x._and(y) is none

    x = none
    y = some('foo')

    assert x._and(y) is none

    x = some(2)
    y = some(3)

    assert x._and(y) == some(3)

    x = y = none

    assert x._and(y) is none

def test_expect():
    assert some(1).expect('cannot fail') == 1

    with pytest.raises(Panic) as err:
        none.expect('definitely will not fail')

    assert str(err.value) == 'definitely will not fail'


def test_Option_as_typehint():
    from typing import Callable, Any
    from contextlib import suppress

    def parse(value: Any, parser: Callable) -> Option[Any]:
        try:
            return some(parser(value))
        except:
            return none

    int_parser = lambda v: int(v)
    assert parse('13', int_parser) == some(13)
    assert parse('Q', int_parser) is none

    with suppress(ImportError):
        from typeguard import typechecked
        from typing import List
        from sys import version_info
        from option import __version_tuple__

        if version_info >= (3, 9):
            List = list

        @typechecked
        def tokenize(value) -> Option[List[str]]:
            if isinstance(value, str):
                return some(list(value))
            elif value == 42:
                return 'Oh no 42!'
            elif value == 13:
                return some(13)
            else:
                return none

        assert tokenize('abc') == some(['a', 'b', 'c'])
        assert tokenize(123) is none

        with pytest.raises(TypeError) as err:
            tokenize(42)

        assert str(err.value) == 'type of the return value must be option.Option; got str instead'

        if False:
            assert tokenize(13) == some(13) # does not throw an error because it yet cannot typecheck the inner value

def test_if_some_do():
    assert (some(20)
                .if_some_do(lambda _: _ / 2)) == 10

    assert (none
                .if_some_do(lambda _: _ * 2)) is none

    assert (some(10)
                .if_some_do(lambda _: some(_ / 2))
                .if_some_do(lambda _: some(_ - 10))
                .if_some_do(lambda _: some(_ + 5))
                .unwrap()) \
                    == 0

def test_lift():
    def addOne(x):
        return x + 1

    addOneToOption = Option.lift(addOne)

    assert addOneToOption(some(1)) == some(2)