from imports import *



def test_ok_flatten():
    assert ok(ok(VALUE)).flatten() == ok(VALUE)
    assert ok(ok(ok(VALUE))).flatten().flatten() == ok(VALUE)
    assert ok(err(VALUE)).flatten() == err(VALUE)

    import pytest
    with pytest.raises(AssertionError) as e:
        ok(VALUE).flatten()

def test_err_flatten():
    assert err(VALUE).flatten() == err(VALUE)

def test_flatten_class_method_form():
    assert Result.flatten(err(VALUE)) == err(VALUE)