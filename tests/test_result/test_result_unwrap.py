from imports import *


def test_ok_unwrap():
    assert ok(VALUE).unwrap() == VALUE

def test_err_unwrap():
    import pytest
    with pytest.raises(Panic) as e:
        err(VALUE).unwrap()


def test_unwrap_class_method_form():
    assert Result.unwrap(ok(VALUE)) == VALUE
