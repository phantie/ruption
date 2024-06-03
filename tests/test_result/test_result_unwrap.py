from ruption import *

def test_ok_unwrap():
    assert ok(1).unwrap() == 1

def test_err_unwrap():
    import pytest
    with pytest.raises(Panic) as e:
        err(0).unwrap()