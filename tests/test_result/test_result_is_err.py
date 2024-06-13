from imports import *



def test_ok_is_err():
    assert not ok(VALUE).is_err()

def test_err_is_err():
    assert err(VALUE).is_err()


def test_is_err_class_method_form():
    assert not Result.is_err(ok(VALUE))
