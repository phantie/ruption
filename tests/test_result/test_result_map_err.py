from imports import *



def test_ok_map_err():
    assert ok(VALUE).map_err(lambda e: ...).is_ok()

def test_err_map_err():
    assert err(2).map_err(lambda e: e * 2).unwrap_err() == 4