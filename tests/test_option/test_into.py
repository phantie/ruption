from ruption import *


def test_converts_python_None_into_option_none():
    assert Option.into(None).is_none()

def test_option_into_returns_option_some_if_arg_is_not_None():
    assert isinstance(Option.into(13), some)

def test_converts_not_None_into_option_some():
    some_value = "Me not none, me some."
    assert Option.into(some_value) == some(some_value)
