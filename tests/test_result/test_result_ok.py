from imports import *



def test_ok_ok():
    assert ok(VALUE).ok() == some(VALUE)

def test_err_ok():
    err(VALUE).ok().is_none()


def test_ok_class_method_form():
    assert Result.ok(ok(VALUE)) == some(VALUE)
