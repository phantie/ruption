from typing import NewType, Callable, TypeVar, Any

__all__ = ["E","P","T","V","R","D","I"]

T = Any            # stored here
I = TypeVar('I')            # inner value

E = NewType('E', Exception) # error
P = NewType('P', Callable)  # predicate
V = TypeVar('V')            # stored there
R = TypeVar('R')            # result
D = TypeVar('D')            # default
