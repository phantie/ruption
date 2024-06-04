from ruption import *
from util import VALUE, VALUE_TYPE


def test_some_expect():
    assert ok(VALUE).expect("") == VALUE

def test_none_expect():
    import pytest
    msg = "to panic"
    with pytest.raises(Panic) as e:
        none().expect(msg)
    assert str(e.value) == msg