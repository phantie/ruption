from imports import *



def test_ok_unwrap_or():
    assert ok(VALUE).unwrap_or(OTHER_VALUE) == VALUE

def test_err_unwrap_or():
    assert err(VALUE).unwrap_or(OTHER_VALUE) == OTHER_VALUE