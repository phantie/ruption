from ruption import *
from util import VALUE, OTHER_VALUE

def test_zip():
    x = some(VALUE)
    y = some(OTHER_VALUE)
    z = none()

    assert x.zip(y) == some((VALUE, OTHER_VALUE))
    assert x.zip(z).is_none()
    assert y.zip(z).is_none()
    assert z.zip(z).is_none()
