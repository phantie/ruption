from imports import *



def test_ok_expect_err():
    import pytest
    msg = ""
    with pytest.raises(Panic) as e:
        assert not ok(VALUE).expect_err(msg)

    assert str(e.value) == msg

def test_err_expect_err():
    assert err(VALUE).expect_err("") == VALUE