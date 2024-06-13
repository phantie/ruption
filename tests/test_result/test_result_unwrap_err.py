from imports import *



def test_ok_is_err():
    import pytest
    with pytest.raises(Panic) as e:
        assert not ok(VALUE).unwrap_err()

def test_err_is_err():
    assert err(VALUE).unwrap_err() == VALUE



def test_unwrap_err_class_method_form():
    assert Result.unwrap_err(err(VALUE)) == VALUE
