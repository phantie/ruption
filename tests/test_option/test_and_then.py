from ruption import *
from util import VALUE, VALUE_TYPE


def test_and_then():
    square = lambda x: some(x * x)

    assert some(2).and_then(square).and_then(square) == some(16)
    assert some(13).and_then(lambda x: none()).is_none()
    assert some(33).and_then(lambda x: none()).and_then(square).is_none()
    assert none().and_then(square).is_none()