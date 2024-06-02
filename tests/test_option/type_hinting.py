"""Quickly check generated typehints by hovering over called method name"""

from ruption import *


def unwrap():
    a: Option = ...
    a.unwrap()
    a: Option[int] = ...
    a.unwrap()
    lambda: none.unwrap()
    some(1).unwrap()

def filter():
    a: Option = ...
    a.filter()
    a: Option[int] = ...
    a.filter()
    lambda: none.filter()
    some(1).filter()

