from ruption import *
from util import VALUE

def test_ok_is_err():
    import pytest
    with pytest.raises(Panic) as e:
        assert not ok(VALUE).unwrap_err()

def test_err_is_err():
    assert err(VALUE).unwrap_err() == VALUE