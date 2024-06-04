from ruption import *
from util import VALUE

def test_ok_flatten():
    assert ok(ok(VALUE)).flatten() == ok(VALUE)
    assert ok(ok(ok(VALUE))).flatten().flatten() == ok(VALUE)
    assert ok(err(VALUE)).flatten() == err(VALUE)

def test_err_flatten():
    assert err(VALUE).flatten() == err(VALUE)