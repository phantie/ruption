from imports import *



def test_ok_iter():
    assert list(ok(VALUE).iter()) == [VALUE]

def test_err_iter():
    assert list(err(VALUE).iter()) == []


def test_iter_class_method_form():
    assert list(Result.iter(ok(VALUE))) == [VALUE]
