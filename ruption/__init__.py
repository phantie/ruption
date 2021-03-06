"""
Implementation of Rusts Option Enum in python. https://doc.rust-lang.org/std/option/enum.Option.html .
A step towards writing more reliable software in python.

Methods not suitable for python, regarding pointers, immutability, etc - are not implemented.

Due to "None" being reserved, "Some and None" are renamed to "some and none".

These methods are also renamed:

    and: also / _and
    or: otherwise / _or

Changed func. signatures:

    unwrap_or_default: added `type` argument because python cannot infer type
    zip: no limits for positional arguments
    zip_with: no limits for positional arguments, and required kw-only callable `f`
    flatten: got `times` argument to flatten an object several times, .flatten(2) == .flatten().flatten()
    
Install:
    
    pip install git+https://github.com/phantie/ruption.git -U

Import:

    from ruption import Option, some, none, Panic
"""
from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import NewType, Callable, Any, Iterable, TypeVar, Generic, Union, Tuple, Type


__all__ = ['Option', 'some', 'none', 'Panic']
__version__ = 1, 4, 1


E = NewType('E', Exception) # error
P = NewType('P', Callable)  # predicate
T = TypeVar('T')            # stored here
V = TypeVar('V')            # stored there
R = TypeVar('R')            # result
D = TypeVar('D')            # default

class Panic(Exception): ...

class Option(Generic[T], metaclass=ABCMeta):

    @classmethod
    def into(cls, value):
        if value is None: return none
        elif isinstance(value, some) or value is none: return value
        else: return some(value)

    @classmethod
    def lift(cls, f: Callable[[Any], Any]) -> Callable[[some], some]:
        """
            def addOne(x):
                return x + 1

            addOneToOption = Option.lift(addOne)

            assert addOneToOption(Some(1)) == Some(2)
        """
        from functools import wraps

        @wraps(f)
        def wrap(s: some):
            return some(f(s.unwrap()))

        return wrap

    @abstractmethod
    def unwrap(self) -> Union[T, E]: ...

    @abstractmethod
    def unwrap_or(self, another: V) -> Union[T, V]: ...

    @classmethod
    @abstractmethod
    def is_none(self) -> bool: ...

    @classmethod
    @abstractmethod
    def is_some(self) -> bool: ...

    @abstractmethod
    def contains(self, value: Any) -> bool: ...

    @abstractmethod
    def unwrap_or_else(self, f: Callable[[], V]) -> Union[T, V]: ...

    @abstractmethod
    def map(self, f: Callable[[T], R]) -> Option[R]: ...

    @abstractmethod
    def map_or(self, default: D, f: Callable[[T], R]) -> Union[D, Option[R]]: ...

    @abstractmethod
    def map_or_else(self, default: Callable[[], D], f: Callable[[T], R]) -> Union[D, Option[R]]: ...

    @abstractmethod
    def iter(self) -> Iterable: ...
    
    @abstractmethod
    def also(self, another: Option) -> Option: ...

    def _and(self, another: Option) -> Option:
        return self.also(another)

    @abstractmethod
    def and_then(self, f: Callable[[T], R]) -> Option[R]: ...

    @abstractmethod
    def filter(self, P: P) -> Option: ...

    @abstractmethod
    def otherwise(self, another: Option) -> Option: ...

    def _or(self, another: Option) -> Option:
        return self.otherwise(another)
    
    @abstractmethod
    def or_else(self, f: Callable[[], R]) -> Union[T, R]: ...

    @abstractmethod
    def xor(self, optb: Option) -> Option: ...

    @abstractmethod
    def zip(self, another: Option) -> Option[Tuple[T, V]]: ...

    @abstractmethod
    def zip_with(self, another: Option, f: Callable[[T, V], R]) -> Option[R]: ...

    @abstractmethod
    def copied(self) -> Option: ...

    @abstractmethod
    def cloned(self) -> Option: ...

    @abstractmethod
    def expect(self, msg: str) -> Union[T, E]: ...

    @abstractmethod
    def expect_none(self) -> Union[None, E]: ...

    @abstractmethod
    def unwrap_none(self) -> Union[None, E]: ...

    @abstractmethod
    def unwrap_or_default(self, type: Type) -> Union[T, R]: ...

    @abstractmethod
    def flatten(self, times = 1) -> Union[T, Option[T]]: ...

    @abstractmethod
    def if_some_do(self, f: Callable[[T], R]) -> Union[R, none]: ...


class some(Option):

    def __init__(self, T: T):
        self.T = T

    def __str__(self):
        return f'Option.some({self.T !r})'

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
        raise Panic('value is ' + str(self))

    def unwrap_none(self): 
        raise self.expect_none()

    def unwrap_or_default(self, type):
        return self.unwrap()

    def flatten(self, times = 1):
        not_zero = times - 1
        if not_zero:
            result = self.flatten()
            for i in range(not_zero):
                result = result.flatten()
            return result
        else:
            return self.T

    def if_some_do(self, f):
        return f(self.T)


def init(cls): return cls()

@init
class none(Option):

    def __bool__(self):
        return False

    def __str__(self):
        return 'Option.none'

    def __repr__(self):
        return str(self)

    def unwrap(self):
        raise Panic('called `Option.unwrap()` on a `none` value')

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
        raise Panic(msg)

    def expect_none(self): ...

    def unwrap_none(self):
        return self

    def unwrap_or_default(self, type):
        return type()

    def flatten(self, times = 1):
        return self

    def if_some_do(self, f):
        return self