from imports import *



def test_ok_map_or_else():
    assert ok(2).map_or_else(lambda e: 42, lambda v: v * 2) == 4

def test_err_map_or_else():
    assert err(2).map_or_else(lambda e: e * 3, lambda v: v * 2) == 6



def test_map_or_else_class_method_form():
    assert Result.map_or_else(ok(2), lambda e: 42, lambda v: v * 2) == 4
