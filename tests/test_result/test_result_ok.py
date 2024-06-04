from ruption import *
from util import *

def test_ok_ok():
    assert ok(VALUE).ok() == some(VALUE)

def test_err_ok():
    err(VALUE).ok().is_none()