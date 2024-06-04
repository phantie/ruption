from ruption.result import *
from util import VALUE

def test_ok_is_ok():
    assert ok(VALUE).is_ok()

def test_err_is_ok():
    assert not err(VALUE).is_ok()