""" Implementation of Rusts Option Enum in python. https://doc.rust-lang.org/std/option/enum.Option.html .
    A step towards writing more reliable sofware in python.

    Methods not suitable for python, for ex. whose which deal with pointers, refs, etc are not implemented.

    Because None is a reserved word, "Some and None" became "some and none".

    Methods renamed for the same reason:
        and: also / _and
        or: otherwise / _or

    Changed func. signatures:
        unwrap_or_default: added 'type' argument considering python cannot infer type
        zip: unlimited amount of positional arguments available
        zip_with: unlimited amount of positional arguments, and required kwonly argument 'f'

    Preferred usage:
    from option.prelude import *
"""

from abc import ABC, abstractmethod
from typing import NewType, Callable, Any, Iterable
from option.exceptions import *

__version__ = '1.1'

E = NewType('E', Exception) # error
P = NewType('P', Callable)  # predicate
T = NewType('T', Any)       # T-Dog
OptionType = \
    NewType('OptionType', T)

def instancer(cls):
    return cls()

class Option:
    def __new__(cls, value):
        return cls.into(value)


    @classmethod
    def into(cls, value):
        if value is None:
            return none
        elif isinstance(value, some) or value is none:
            return value
        else:
            return some(value)

    class OptionInterface(ABC):
        @abstractmethod
        def unwrap(self): ...

        @abstractmethod
        def unwrap_or(self, another: OptionType): ...

        @classmethod
        @abstractmethod
        def is_none(self): ...

        @classmethod
        @abstractmethod
        def is_some(self): ...

        @abstractmethod
        def contains(self, value: T): ...

        @abstractmethod
        def unwrap_or_else(self, f: Callable[[], T]): ...

        @abstractmethod
        def map(self, f: Callable[[T], Any]): ...

        @abstractmethod
        def map_or(self, default: Any, f: Callable[[T], Any]): ...

        @abstractmethod
        def map_or_else(self, default: Callable[[], Any], f: Callable[[T], Any]): ...

        @abstractmethod
        def iter(self) -> Iterable: ...
        
        @abstractmethod
        def also(self, another): ...

        def _and(self, another):
            return self.also(another)

        @abstractmethod
        def and_then(self, f: Callable[[T], Any]): ...

        @abstractmethod
        def filter(self, P: P): ...

        @abstractmethod
        def otherwise(self, another: OptionType): ...

        def _or(self, another: OptionType):
            return self.otherwise(another)
        
        @abstractmethod
        def or_else(self, f: Callable[[], Any]): ...

        @abstractmethod
        def xor(self, optb: OptionType): ...

        @abstractmethod
        def zip(self, another: OptionType): ...

        @abstractmethod
        def zip_with(self, another, f: Callable[[T, T], Any]): ...

        @abstractmethod
        def copied(self): ...

        @abstractmethod
        def cloned(self): ...

        @abstractmethod
        def expect(self, msg: str): ...

        @abstractmethod
        def expect_none(self): ...

        @abstractmethod
        def unwrap_none(self): ...

        @abstractmethod
        def unwrap_or_default(self, type: type): ...

        @abstractmethod
        def flatten(self): ...


    class some(OptionInterface):
        def __init__(self, T: T):
            self.T = T

        def __str__(self):
            return f'Option.some({repr(self.T)})'

        def __repr__(self):
            return str(self)

        def unwrap(self):
            return self.T

        def unwrap_or(self, another):
            return self.unwrap()

        @classmethod
        def is_none(cls):
            return False

        @classmethod
        def is_some(cls):
            return True

        def contains(self, value):
            return self.T == value

        def __eq__(self, another):
            return isinstance(another, self.__class__) and self.T == another.T

        def unwrap_or_else(self, f):
            return self.unwrap()

        def map(self, f):
            return some(f(self.T))

        def map_or(self, default, f):
            return self.map(f)

        def map_or_else(self, default, f):
            return self.map(f)

        def iter(self):
            return iter([self.T])

        def also(self, another):
            return another

        def and_then(self, f):
            res = f(self.T)
            if res is none:
                return none

            return some(res)

        def filter(self, P):
            if P(self.T):
                return self
            else:
                return none

        def otherwise(self, another):
            return self

        def or_else(self, f):
            return self

        def xor(self, optb):
            if optb is none:
                return self
            else:
                return none


        def zip(self, *others):
            if len(others) < 1:
                raise TypeError

            if any(el is none for el in others):
                return none

            if any(not isinstance(el, some) for el in others):
                raise TypeError('cannot zip non Option types')

            return some((self.T, *(el.T for el in others )))


        def zip_with(self, *others, f=None):
            if len(others) < 1 or f is None:
                raise TypeError

            if any(el is none for el in others):
                return none

            if any(not isinstance(el, some) for el in others):
                raise TypeError('cannot zip non Option types')

            return some(f(self.T, *(el.T for el in others )))

        def copied(self):
            return some(self.T)

        def cloned(self):
            return self.copied()

        def expect(self, msg):
            return self.T

        def expect_none(self):
            raise noneIsExpected('actual value is ' + str(self))

        def unwrap_none(self): 
            raise self.expect_none()

        def unwrap_or_default(self, type):
            return self.unwrap()

        def flatten(self):
            return self.T

    @instancer
    class none(OptionInterface):
        def __str__(self):
            return 'Option.none'

        def __repr__(self):
            return str(self)

        def unwrap(self):
            raise noneValue

        def unwrap_or(self, another):
            return another

        @classmethod
        def is_none(cls):
            return True

        @classmethod
        def is_some(cls):
            return False

        def contains(self, value):
            return False

        def __eq__(self, another):
            return self is another

        def unwrap_or_else(self, f):
            return f()

        def map(self, f):
            return self

        def map_or(self, default, f):
            return default

        def map_or_else(self, default, f):
            return default()

        def iter(self):
            return iter([self])

        def also(self, another):
            return self

        def and_then(self, f):
            return self

        def filter(self, P):
            return self

        def otherwise(self, another):
            return another

        def or_else(self, f):
            return f()

        def xor(self, optb):
            if optb is not self:
                return optb
            else:
                return self

        def zip(self, *others):
            return self

        def zip_with(self, *others, f=None):
            return self

        def copied(self):
            return self

        def cloned(self):
            return self

        def expect(self, msg):
            raise noneValue(msg)

        def expect_none(self): ...

        def unwrap_none(self):
            return self

        def unwrap_or_default(self, type):
            return type()

        def flatten(self):
            return self

some, none = Option.some, Option.none