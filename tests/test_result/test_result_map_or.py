from imports import *



def test_ok_map_or():
    assert ok(2).map_or(42, lambda v: v * 2) == 4

def test_err_map_or():
    assert err(2).map_or(42, lambda v: v * 2) == 42


def test_map_or_class_method_form():
    assert Result.map_or(ok(2), 42, lambda v: v * 2) == 4
