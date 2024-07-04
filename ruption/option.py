
from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import Callable, Any, Iterator, Generic, Tuple, NoReturn, Literal, Callable, TypeVar

from .panic import Panic


__all__ = ['Option', 'some', 'none']


I = TypeVar('I')            # inner value
U = TypeVar('U')            # use with zip
R = TypeVar('R')            # result


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
            returns inner value if some
            return default if none
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

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.and
    @abstractmethod
    def and_(self, another: Option[R]) -> Option[R]:
        """
            returns none if none
            returns another otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.and_then
    @abstractmethod
    def and_then(self, fn: Callable[[I], Option[R]]) -> Option[R]:
        """
            returns fn applied to inner value if some
            returns none if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.filter
    @abstractmethod
    def filter(self, p: Callable[[I], bool]) -> Option[I]:
        """
            returns some inner value if predicate on inner value is true
            returns none otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.or
    @abstractmethod
    def or_(self, another: Option[I]) -> Option[I]:
        """
            returns some inner value if some
            return none otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.or_else
    @abstractmethod
    def or_else(self, fn: Callable[[], Option[I]]) -> Option[I]:
        """
            returns some value if some
            returns result of calling fn if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.xor
    @abstractmethod
    def xor(self, optb: Option[I]) -> Option[I]:
        """
            returns some value if only one is some
            returns none otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.zip
    @abstractmethod
    def zip(self, another: Option[U]) -> Option[Tuple[I, U]]:
        """
            returns some tuple of left inner value and right inner value if both are some
            returns none otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.zip_with
    @abstractmethod
    def zip_with(self, another: Option[U], fn: Callable[[I, U], R]) -> Option[R]:
        """
            returns some result of fn called with left inner value and right inner value if both are some
            returns none otherwise
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.expect
    @abstractmethod
    def expect(self, msg: str) -> I:
        """
            returns inner value if some
            panics with msg if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.flatten
    @abstractmethod
    def flatten(self) -> Option[I]: 
        """
            returns some value if some some value
            returns none if some none
            returns none value if none
            assertion error if not called on some some value or some none or none
                for example on some value
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.ok_or
    @abstractmethod
    def ok_or(self, error: Err) -> Result[I, Err]:
        """
            returns ok value if some
            returns err error if none
        """

    # https://doc.rust-lang.org/std/option/enum.Option.html#method.inspect
    @abstractmethod
    def inspect(self, fn: Callable[[I], None]) -> Option[I]:
        """
            calls fn on value if some
            returns unmodified value
            fn must not modify value
        """


class some(Option[I]):
    def __init__(self, value: I):
        self.T = value

    def __str__(self):
        return f'Option.some({self.unwrap() !r})'

    def __repr__(self):
        return str(self)
    
    def __eq__(self, another):
        return isinstance(another, self.__class__) and self.unwrap() == another.unwrap()

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
        return self.unwrap() == cmp

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

    def and_(self, another: Option[R]) -> Option[R]:
        return another

    def and_then(self, fn: Callable[[I], Option[R]]) -> Option[R]:
        return fn(self.unwrap())

    def filter(self, p: Callable[[I], bool]) -> Option[I]:
        return self if p(self.unwrap()) else none()
        

    def or_(self, another: Option[I]) -> Option[I]:
        return self

    def or_else(self, fn: Callable[[], Option[I]]) -> Option[I]:
        return self

    def xor(self, optb: Option[I]) -> Option[I]:
        if optb.is_none():
            return self
        else:
            return none()


    def zip(self, another: Option[U]) -> Option[Tuple[I, U]]:
        if another.is_none():
            return none()
        else:
            return some((self.unwrap(), another.unwrap()))


    def zip_with(self, another: Option[U], fn: Callable[[I, U], R]) -> Option[R]:
        if another.is_none():
            return none()
        else:
            return some(fn(self.unwrap(), another.unwrap()))

    def expect(self, msg: str) -> I:
        return self.unwrap()

    def flatten(self) -> Option[I]:
        assert isinstance(self.unwrap(), Option)
        return self.unwrap()

    def ok_or(self, error: Err) -> Result[I, Err]:
        return ok(self.unwrap())

    def inspect(self, fn: Callable[[I], None]) -> Option[I]:
        fn(self.unwrap())
        return self

class none(Option[I]):
    def __bool__(self):
        return False

    def __str__(self):
        return 'Option.none'

    def __repr__(self):
        return str(self)

    def __eq__(self, another):
        return isinstance(another, self.__class__)

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

    def unwrap_or_else(self, fn: Callable[[], I]) -> I:
        """
            returns result of calling fn
        """
        return fn()

    def map(self, fn: Callable[[I], R]) -> Option[R]: # TODO try output none[R]
        """
            returns none
        """
        return none()

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
    
    def and_(self, another: Option[R]) -> Option[R]:
        return none()

    def and_then(self, fn: Callable[[I], Option[R]]) -> Option[R]:
        return none()

    def filter(self, p: Callable[[I], bool]) -> Option[I]: # TODO try none[I]
        return none()

    def or_(self, another: Option[I]) -> Option[I]:
        return another

    def or_else(self, fn: Callable[[], Option[I]]) -> Option[I]:
        return fn()

    def xor(self, optb: Option[I]) -> Option[I]:
        if optb.is_some():
            return optb
        else:
            return none()

    def zip(self, another: Option[U]) -> Option[Tuple[I, U]]:
        return none()

    def zip_with(self, another: Option[U], fn: Callable[[I, U], R]) -> Option[R]:
        return none()

    def expect(self, msg: str) -> I:
        raise Panic(msg)

    def flatten(self) -> Option[I]:
        return none()
    
    def ok_or(self, error: Err) -> Result[I, Err]:
        return err(error)

    def inspect(self, fn: Callable[[I], None]) -> Option[I]:
        return self


from .result import Result, Ok, Err, ok, err