from ruption import *
from util import *

def test_ok_err():
    assert ok(VALUE).err().is_none()

def test_err_err():
    assert err(VALUE).err() == some(VALUE)