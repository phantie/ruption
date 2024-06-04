from ruption import *
from util import VALUE

def test_ok_unwrap():
    assert ok(VALUE).unwrap() == VALUE

def test_err_unwrap():
    import pytest
    with pytest.raises(Panic) as e:
        err(VALUE).unwrap()