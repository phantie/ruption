from ruption import *
from util import VALUE

def test_ok_iter():
    assert list(ok(VALUE).iter()) == [VALUE]

def test_err_iter():
    assert list(err(VALUE).iter()) == []