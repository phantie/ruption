from ruption import *
from util import VALUE

def test_ok_is_err_and():
    assert not ok(2).is_err_and(lambda e: ...)

def test_err_is_err_and():
    assert err(2).is_err_and(lambda v: v == 2)
    assert not err(2).is_err_and(lambda v: v == 3)
