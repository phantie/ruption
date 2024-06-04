import pytest

from ruption import *


def test_option_none_not_equal_to_None():
    assert none() != None

def test_option_none_equals_to_self():
    assert none() == none()

def test_converts_python_None_into_option_none():
    assert Option.into(None).is_none()

def test_option_into_returns_option_some_if_arg_is_not_None():
    assert isinstance(Option.into(13), some)

def test_converts_not_None_into_option_some():
    some_value = "Me not none, me some."
    assert Option.into(some_value) == some(some_value)

def test_some_13_not_equals_some_42():
    assert some(13) != some(42)


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
        def tokenize(value) -> Option[list[str]]:
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


def test_lift():
    def addOne(x):
        return x + 1

    addOneToOption = Option.lift(addOne)

    assert addOneToOption(some(1)) == some(2)