from imports import *



def test_ok_unwrap_or():
    assert ok(VALUE).unwrap_or(OTHER_VALUE) == VALUE

def test_err_unwrap_or():
    assert err(VALUE).unwrap_or(OTHER_VALUE) == OTHER_VALUE



def test_unwrap_or_class_method_form():
    assert Result.unwrap_or(ok(VALUE), OTHER_VALUE) == VALUE
