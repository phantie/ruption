from ruption import *
from util import VALUE, OTHER_VALUE


def test_zip_with():
    def area(a, b):
        return a * b

    x = some(2)
    y = some(3)
    z = none()

    assert x.zip_with(y, area) == some(6)
    assert y.zip_with(z, area).is_none()
    assert x.zip_with(z, area).is_none()