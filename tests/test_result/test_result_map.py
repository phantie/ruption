from imports import *



def type_hinting():
    """Quickly check generated typehints by hovering over called method name"""

    
    def _():
        a: Result = ...
        a.map(lambda value: VALUE)
    a: Result[int, Exception] = ...
    a.map(lambda value: VALUE)
    lambda: err(0).map(lambda value: VALUE).unwrap()

    ok(VALUE).map(lambda x: x * 2).unwrap()



def test_ok_map():
    assert ok(1).map(lambda x: x * 2).unwrap() == 2

def test_err_map():
    import pytest
    with pytest.raises(Panic) as e:
        assert err(1).map(lambda x: x * 2).unwrap()


def test_map_class_method_form():
    assert Result.map(ok(1), lambda x: x * 2).unwrap() == 2
