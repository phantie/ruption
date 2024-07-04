from imports import *

def test_and_then():
    square = lambda x: some(x * x)

    assert some(2).and_then(square).and_then(square) == some(16)
    assert some(13).and_then(lambda x: none()).is_none()
    assert some(33).and_then(lambda x: none()).and_then(square).is_none()
    assert none().and_then(square).is_none()


def test_and_then_class_method_form():
    square = lambda x: some(x * x)

    assert Option.and_then(some(2), square) == some(4)

