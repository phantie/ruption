from imports import *


def test_ok_unwrap_or_else():
    assert ok(VALUE).unwrap_or_else(lambda e: ...) == VALUE

def test_err_unwrap_or_else():
    assert err(2).unwrap_or_else(lambda e: e * 2) == 4


def test_unwrap_or_else_class_method_form():
    assert Result.unwrap_or_else(ok(VALUE), lambda e: ...) == VALUE
