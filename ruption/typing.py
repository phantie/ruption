from typing import NewType, Callable, TypeVar

__all__ = ["E","P","T","V","R","D"]

E = NewType('E', Exception) # error
P = NewType('P', Callable)  # predicate
T = TypeVar('T')            # stored here
V = TypeVar('V')            # stored there
R = TypeVar('R')            # result
D = TypeVar('D')            # default

