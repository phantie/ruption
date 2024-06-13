from imports import *


def test_ok_err():
    assert ok(VALUE).err().is_none()

def test_err_err():
    assert err(VALUE).err() == some(VALUE)

def test_err_class_method_form():
    assert Result.ok(err(VALUE)).is_none()
    assert Result.err(err(VALUE)) == some(VALUE)