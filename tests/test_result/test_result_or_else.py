from imports import *



def sq(x: int) -> Result[int, int]:
    return ok(x * x)

def error(x: int) -> Result[int, int]:
    return err(x)

def test_ok_or_else():
    assert ok(2).or_else(sq) == ok(2)
    assert ok(2).or_else(sq).or_else(sq) == ok(2)
    assert ok(2).or_else(error).or_else(sq) == ok(2)

def test_err_or_else():
    assert err(3).or_else(sq).or_else(error) == ok(9)
    assert err(3).or_else(error).or_else(error) == err(3)


def test_or_else_class_method_form():
    assert Result.or_else(ok(2), sq) == ok(2)
