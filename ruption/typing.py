from typing import NewType, Callable, TypeVar, Any

__all__ = ["E","P","T","V","R","D","I","U"]

I = TypeVar('I')            # inner value
U = TypeVar('U')            # use with zip
R = TypeVar('R')            # result

T = Any            # stored here

E = NewType('E', Exception) # error
P = NewType('P', Callable)  # predicate
V = TypeVar('V')            # stored there
D = TypeVar('D')            # default
