from ruption.result import *
from util import VALUE

def test_ok_is_err():
    assert not ok(VALUE).is_err()

def test_err_is_err():
    assert err(VALUE).is_err()