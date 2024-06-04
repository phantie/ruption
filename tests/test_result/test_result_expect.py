from imports import *


def test_ok_expect():
    assert ok(VALUE).expect("") == VALUE

def test_err_expect():
    import pytest
    msg = "to panic"
    with pytest.raises(Panic) as e:
        err(VALUE).expect(msg)
    assert str(e.value) == msg