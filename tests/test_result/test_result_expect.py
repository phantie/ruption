from imports import *


def test_ok_expect():
    assert ok(VALUE).expect("") == VALUE

def test_err_expect():
    import pytest
    msg = "to panic"
    with pytest.raises(Panic) as e:
        err(VALUE).expect(msg)
    assert str(e.value) == msg


def test_expect_class_method_form():
    assert Result.expect(ok(VALUE), "") == VALUE