from imports import *



def test_ok_is_ok():
    assert ok(VALUE).is_ok()

def test_err_is_ok():
    assert not err(VALUE).is_ok()