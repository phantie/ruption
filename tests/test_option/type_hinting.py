"""Quickly check generated typehints by hovering over called method name"""

from ruption import *


def unwrap():
    def _():
        a: Option = ...
        a.unwrap()
    a: Option[int] = ...
    a.unwrap()
    lambda: none.unwrap()
    lambda: none[int].unwrap()
    some(1).unwrap()

def filter():
    def _():
        a: Option = ...
        a.filter()
    a: Option[int] = ...
    a.filter()
    none.filter(lambda x: x > 0)
    none[int].filter(lambda x: x > 0)
    some(1).filter()

def unwrap_or():
    def _():
        a: Option = ...
        a.unwrap_or(0)
    a: Option[int] = ...
    a.unwrap_or(0)
    none.unwrap_or(1)
    none[int].unwrap_or(1)
    some(1).unwrap_or(0)
