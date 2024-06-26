from imports import *



def test_ok_is_err_and():
    assert not ok(2).is_err_and(lambda e: ...)

def test_err_is_err_and():
    assert err(2).is_err_and(lambda v: v == 2)
    assert not err(2).is_err_and(lambda v: v == 3)


def test_is_err_and_class_method_form(capsys):
    assert not Result.is_err_and(ok(2), lambda e: ...)
