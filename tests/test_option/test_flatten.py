from ruption import *
from util import VALUE, VALUE_TYPE



def test_flatten():
    assert some(some(VALUE)).flatten() == some(VALUE)
    assert some(some(some(VALUE))).flatten().flatten() == some(VALUE)
    assert none().flatten().is_none()

    import pytest
    with pytest.raises(AssertionError) as e:
        some(VALUE).flatten()