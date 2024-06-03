import pytest

from ruption import *


def test_option_none_not_equal_to_None():
    assert none() != None

# @pytest.skip
# def test_option_none_equals_to_self():
#     assert none() == none()

def test_converts_python_None_into_option_none():
    assert Option.into(None).is_none()

def test_option_into_returns_option_some_if_arg_is_not_None():
    assert isinstance(Option.into(13), some)

def test_converts_not_None_into_option_some():
    some_value = "Me not none, me some."
    assert Option.into(some_value) == some(some_value)

def test_some_13_not_equals_some_42():
    assert some(13) != some(42)


def test_map_or_else_on_none_executes_function_that_changes_state():
    def change_state_of_local_var():
        nonlocal local
        local += 6
        
    local = 14

    none().map_or_else(change_state_of_local_var, lambda: None)
    assert local == 20


def test_and_then():
    square = lambda x: some(x**2)

    assert some(2).and_then(square).and_then(square) == some(16)
    assert some(13).and_then(lambda self: none()).is_none()
    assert some(33).and_then(lambda self: none()).and_then(square).is_none()
    assert none().and_then(lambda x: x**2).is_none()


def test_otherwise():
    a, b = some(3), none()

    assert a.otherwise(b) == a
    assert b.otherwise(a) == a
    assert a.otherwise(some(4)) == a
    assert b.otherwise(b) is b

def test__or():
    a, b = some(3), none()

    assert a._or(b) == a
    assert b._or(a) == a
    assert a._or(some(4)) == a
    assert b._or(b) is b

def test_or_else():
    nobody = lambda: none()
    vikings = lambda: some('vikings')

    assert some('barbarians').or_else(vikings) == some('barbarians')
    assert none().or_else(vikings) == some('vikings')
    assert none().or_else(nobody).is_none()

def test_xor():
    x, y = some(2), none()
    assert x.xor(y) == some(2)

    x, y = none(), some(2)
    assert x.xor(y) == some(2)

    x = y = some(2)
    assert x.xor(y).is_none()

    x = y = none()
    assert x.xor(y).is_none()


def test_zip():
    x = some(1)
    y = some('hey')
    z = none()

    assert x.zip(y) == some((1, 'hey'))
    assert x.zip(z).is_none()
    assert z.zip(z).is_none()

def test_zip_advanced():
    x = some(1)
    y = some(2)
    z = none()

    assert x.zip(y)
    assert x.zip(z).is_none()

def test_zip_with():
    def area(a, b):
        return a*b

    x = some(1)
    y = some(2)
    z = none()

    assert x.zip_with(y, area) == some(2)
    assert x.zip_with(z, area).is_none

def test_copied():
    x = some('num')
    y = x.copied()
    assert not x is y

    # there`s no point in actual copy of none. so it`s ommitted.
    assert none().copied().is_none()


def test_expect_none():
    with pytest.raises(Panic):
        some(1).expect_none()

    assert none().expect_none() is None

def test_unwrap_none():
    with pytest.raises(Panic):
        some(1).unwrap_none()

    assert none().unwrap_none().is_none()

def test_unwrap_or_default():
    assert some(1).unwrap_or_default(int) == 1
    assert none().unwrap_or_default(int) == 0
    assert none().unwrap_or_default(list) == []

def test_flatten():
    assert some(1) == some(some(1)).flatten()
    assert 1 == some(some(1)).flatten().flatten()
    assert some(1) == some(some(some(1))).flatten().flatten()
    assert some(none()).flatten().is_none()
    assert none().flatten().is_none()

    assert 1 == some(some(1)).flatten(2)
    assert some(1) == some(some(some(1))).flatten(2)
    assert some(none()).flatten(13).is_none()
    assert none().flatten(13).is_none()


def test_also():
    x = some(2)
    y = none()

    assert x.also(y).is_none()

    x = none()
    y = some('foo')

    assert x.also(y).is_none()

    x = some(2)
    y = some(3)

    assert x.also(y) == some(3)

    x = y = none()

    assert x.also(y).is_none()

def test__and():
    x = some(2)
    y = none()

    assert x._and(y).is_none()

    x = none()
    y = some('foo')

    assert x._and(y).is_none()

    x = some(2)
    y = some(3)

    assert x._and(y) == some(3)

    x = y = none()

    assert x._and(y).is_none()

def test_expect():
    assert some(1).expect('cannot fail') == 1

    with pytest.raises(Panic) as err:
        none().expect('definitely will not fail')

    assert str(err.value) == 'definitely will not fail'


def test_Option_as_typehint():
    from typing import Callable, Any
    from contextlib import suppress

    def parse(value: Any, parser: Callable) -> Option[Any]:
        try:
            return some(parser(value))
        except:
            return none()

    int_parser = lambda v: int(v)
    assert parse('13', int_parser) == some(13)
    assert parse('Q', int_parser).is_none()

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
        assert tokenize(123).is_none()

        with pytest.raises(TypeError) as err:
            tokenize(42)

        assert str(err.value) == 'type of the return value must be option.Option; got str instead'

        if False:
            assert tokenize(13) == some(13) # does not throw an error because it yet cannot typecheck the inner value

def test_if_some_do():
    assert (some(20)
                .if_some_do(lambda _: _ / 2)) == 10

    assert (none()
                .if_some_do(lambda _: _ * 2)).is_none()

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