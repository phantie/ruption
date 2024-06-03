
from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import Callable, Any, Iterator, Generic, Union, Tuple, Type, NoReturn, Literal

from .typing import *
from .panic import Panic

__all__ = ['Option', 'some', 'none']

class Option(Generic[I], metaclass=ABCMeta):
    # https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap
    @abstractmethod
    def unwrap(self) -> I:
        """
            returns inner value if some,
            panics if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_or
    @abstractmethod
    def unwrap_or(self, default: I) -> I:
        """
            returns inner value or default
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.is_none
    @abstractmethod
    def is_none(self) -> bool:
        """
            returns true if none
            returns false if some
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.is_some
    @abstractmethod
    def is_some(self) -> bool:
        """
            returns true if some
            returns false if none
        """

    # was removed from latest rust, with recommendation to use is_some_and instead
    @abstractmethod
    def contains(self, cmp: I) -> bool:
        """
            returns true if is some and inner value equals to cmp
            returns false otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_or_else
    @abstractmethod
    def unwrap_or_else(self, fn: Callable[[], I]) -> I:
        """
            returns inner value if some
            returns result of calling fn if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.map
    @abstractmethod
    def map(self, fn: Callable[[I], R]) -> Option[R]:
        """
            returns some value transformed with fn if some
            returns none if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.map_or
    @abstractmethod
    def map_or(self, default: R, fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some value transformed with fn if some
            returns some default if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.map_or_else
    @abstractmethod
    def map_or_else(self, default: Callable[[], R], fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some value transformed with fn if some
            returns some result of calling default if none
        """

    @abstractmethod
    def iter(self) -> Iterator[I]:
        """
            returns iterator yielding inner value once if some
            returns empty iterator if none
        """
    
    @abstractmethod
    def also(self, another: Option) -> Option: ...

    def _and(self, another: Option) -> Option:
        return self.also(another)

    @abstractmethod
    def and_then(self, f: Callable[[T], R]) -> Option[R]: ...

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.filter
    @abstractmethod
    def filter(self, p: Callable[[I], bool]) -> Option[I]: ...

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


class some(Option[I]):
    def __init__(self, value: I):
        self.T = value

    def __str__(self):
        return f'Option.some({self.T !r})'

    def __repr__(self):
        return str(self)

    def unwrap(self) -> I:
        """returns inner value"""
        return self.T

    def unwrap_or(self, default: I) -> I:
        return self.unwrap()

    def is_none(self) -> Literal[False]:
        """
            returns false
        """
        return False

    def is_some(self) -> Literal[True]:
        """
            returns true
        """
        return True

    def contains(self, cmp: I) -> bool:
        """
            returns true if inner value equals to cmp
        """
        return self.T == cmp

    def __eq__(self, another):
        return isinstance(another, self.__class__) and self.T == another.T

    def unwrap_or_else(self, fn: Callable[[], I]) -> I:
        """
            returns inner value
        """
        return self.unwrap()

    def map(self, fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some value transformed with fn
        """
        return some(fn(self.unwrap()))

    def map_or(self, default: R, fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some value transformed with fn
        """
        return self.map(fn)

    def map_or_else(self, default: Callable[[], R], fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some value transformed with fn
        """
        return self.map(fn)

    def iter(self) -> Iterator[I]:
        """
            returns iterator yielding inner value once
        """
        return [self.unwrap()].__iter__()

    def also(self, another):
        return another

    def and_then(self, f):
        res = f(self.T)
        if res is none:
            return none

        return some(res)

    def filter(self, p: Callable[[I], bool]) -> Option[I]:
        return self if p(self.T) else none
        

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


class none(Option[I]):
    def __bool__(self):
        return False

    def __str__(self):
        return 'Option.none'

    def __repr__(self):
        return str(self)

    def unwrap(self) -> NoReturn:
        """panics"""
        raise Panic('called `Option.unwrap()` on a `none` value')

    def unwrap_or(self, default: I) -> I:
        return default

    def is_none(self) -> Literal[True]:
        """
            returns true
        """
        return True

    def is_some(self) -> Literal[False]:
        """
            returns false
        """
        return False

    def contains(self, cmp: I) -> Literal[False]:
        """
            returns false
        """
        return False

    def __eq__(self, another):
        return self is another

    def unwrap_or_else(self, fn: Callable[[], I]) -> I:
        """
            returns result of calling fn
        """
        return fn()

    def map(self, fn: Callable[[I], R]) -> Option[R]: # TODO try output none[R]
        """
            returns none
        """
        return self

    def map_or(self, default: R, fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some default
        """
        return some(default)

    def map_or_else(self, default: Callable[[], R], fn: Callable[[I], R]) -> Option[R]: # TODO try output some[R]
        """
            returns some result of calling default
        """
        return some(default())

    def iter(self) -> Iterator[I]:
        """
            returns empty iterator
        """
        return [].__iter__()

    def also(self, another):
        return self

    def and_then(self, f):
        return self

    def filter(self, p: Callable[[I], bool]) -> none:
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

none = none()