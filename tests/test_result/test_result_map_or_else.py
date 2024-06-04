from ruption import *
from util import VALUE

def test_ok_map_or_else():
    assert ok(2).map_or_else(lambda e: 42, lambda v: v * 2) == 4

def test_err_map_or_else():
    assert err(2).map_or_else(lambda e: e * 3, lambda v: v * 2) == 6