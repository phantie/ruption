from imports import *



def test_ok_is_ok():
    assert ok(VALUE).is_ok()

def test_err_is_ok():
    assert not err(VALUE).is_ok()

def test_is_ok_class_method_form():
    assert list(map(Result.unwrap, filter(Result.is_ok, [ok(123), err("")]))) == [123]
