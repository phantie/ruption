from typing import NewType, Callable, TypeVar, Any

__all__ = ["E","P","T","V","R","D","O"]

E = NewType('E', Exception) # error
P = NewType('P', Callable)  # predicate
T = Any            # stored here
V = TypeVar('V')            # stored there
R = TypeVar('R')            # result
D = TypeVar('D')            # default

O = TypeVar('O') # for Option generality