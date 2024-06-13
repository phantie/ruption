from imports import *



def test_ok_is_ok_and():
    assert ok(2).is_ok_and(lambda v: v == 2)
    assert not ok(2).is_ok_and(lambda v: v == 3)

def test_err_is_ok_and():
    assert not err(VALUE).is_ok_and(lambda e: ...)


def test_is_ok_and_class_method_form():
    assert Result.is_ok_and(ok(2), lambda v: v == 2)
