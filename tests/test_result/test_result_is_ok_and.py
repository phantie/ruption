from ruption import *
from util import VALUE

def test_ok_is_ok_and():
    assert ok(2).is_ok_and(lambda v: v == 2)
    assert not ok(2).is_ok_and(lambda v: v == 3)

def test_err_is_ok_and():
    assert not err(VALUE).is_ok_and(lambda e: ...)