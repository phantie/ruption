from ruption import *
from util import VALUE

def test_ok_map_or():
    assert ok(2).map_or(42, lambda v: v * 2) == 4

def test_err_map_or():
    assert err(2).map_or(42, lambda v: v * 2) == 42