
from __future__ import annotations
from abc import abstractmethod
from typing import Callable, Iterator, Generic, NoReturn, TypeVar

from .panic import Panic
from ._class_method_form import ClassMethodFormMeta
from .panic import _panic


__all__ = ['Result', 'ok', 'err', 'Ok', 'Err']


Ok = TypeVar("Ok")
Err = TypeVar("Err")
R = TypeVar("R")




class Result(Generic[Ok, Err], metaclass=ClassMethodFormMeta):
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap
    @abstractmethod
    def unwrap(self) -> Ok:
        """
            returns inner value if ok
            panics if err
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.map
    @abstractmethod
    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]:
        """
            returns ok value transformed with fn if some
            returns none if none
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.is_ok
    @abstractmethod
    def is_ok(self) -> bool:
        """
            returns true if ok
            returns false if err
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.is_err
    @abstractmethod
    def is_err(self) -> bool:
        """
            returns true if err
            returns false if ok
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap_err
    @abstractmethod
    def unwrap_err(self) -> Err:
        """
            returns inner value if err
            panics if ok
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.expect
    @abstractmethod
    def expect(self, msg: str) -> Ok:
        """
            returns inner value if ok
            panics with msg if err
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.ok
    @abstractmethod
    def ok(self) -> Option[Ok]:
        """
            converts Result to Option discarding error
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap_or
    @abstractmethod
    def unwrap_or(self, default: Ok) -> Ok:
        """
            returns inner value if some
            return default if none
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap_or_else
    @abstractmethod
    def unwrap_or_else(self, fn: Callable[[Err], Ok]) -> Ok:
        """
            returns inner value if some
            returns result of fn calling on error if err
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.map_err
    @abstractmethod
    def map_err(self, fn: Callable[[Err], R]) -> Result[Ok, R]:
        """
            returns ok value if some
            returns err result of fn calling on error if err
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.inspect_err
    @abstractmethod
    def inspect_err(self, fn: Callable[[Err], None]) -> Result[Ok, Err]:
        """
            calls fn on value if err
            returns unmodified value
            fn must not modify value
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.inspect
    @abstractmethod
    def inspect(self, fn: Callable[[Ok], None]) -> Result[Ok, Err]:
        """
            calls fn on value if some
            returns unmodified value
            fn must not modify value
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.expect_err
    @abstractmethod
    def expect_err(self, msg: str) -> Err:
        """
            returns inner value if err
            panics with msg if ok
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.is_ok_and
    @abstractmethod
    def is_ok_and(self, fn: Callable[[Ok], bool]) -> bool:
        """
            returns true if ok and result of fn calling on value is true
            returns false otherwise
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.flatten
    @abstractmethod
    def flatten(self) -> Result[Ok, Err]:
        """
            returns ok value if ok ok value
            returns err value if ok err value
            returns err value if err
            assertion error if not called on ok ok value or ok err value or err value
                for example on ok value
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.iter
    @abstractmethod
    def iter(self) -> Iterator[Ok]:
        """
            returns iterator yielding inner value once if ok
            returns empty iterator if err
        """

   
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.err
    @abstractmethod
    def err(self) -> Option[Err]:
        """
            converts Result to Option discarding ok value
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.is_err_and
    @abstractmethod
    def is_err_and(self, fn: Callable[[Err], bool]) -> bool:
        """
            returns true if err and result of calling fn on value is true
            returns false otherwise
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.map_or
    @abstractmethod
    def map_or(self, default: R, fn: Callable[[Ok], R]) -> R:
        """
            returns result of calling fn on value if ok
            returns default if err
        """
    
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.map_or_else
    @abstractmethod
    def map_or_else(self, default: Callable[[Err], R], fn: Callable[[Ok], R]) -> R:
        """
            returns result of calling fn on value if ok
            returns result of calling default on value if err
        """

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.or_else
    @abstractmethod
    def or_else(self, fn: Callable[[Err], Result[Ok, R]]) -> Result[Ok, R]:
        """
            returns ok value if ok
            returns result of calling fn on value if err
        """

class ok(Result[Ok, Err]):
    def __init__(self, value: Ok):
        self.T = value

    def __str__(self):
        return f'Result.ok({self.unwrap()!r})'
    
    def __repr__(self):
        return str(self)

    def __eq__(self, another):
        return isinstance(another, self.__class__) and self.unwrap() == another.unwrap()

    def unwrap(self) -> Ok:
        return self.T
    
    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]:
        return ok(fn(self.unwrap()))

    def is_ok(self) -> bool:
        return True
    
    def is_err(self) -> bool:
        return False
    
    def unwrap_err(self) -> NoReturn:
        raise Panic("called .unwrap_err() on ok")
    
    def expect(self, msg: str) -> Ok:
        return self.unwrap()

    def ok(self) -> Option[Ok]:
        return some(self.unwrap())
    
    def unwrap_or(self, default: Ok) -> Ok:
        return self.unwrap()

    def unwrap_or_else(self, fn: Callable[[Err], Ok]) -> Ok:
        return self.unwrap()
    
    def map_err(self, fn: Callable[[Err], R]) -> Result[Ok, R]:
        return self
    
    def inspect_err(self, fn: Callable[[Err], None]) -> Result[Ok, Err]:
        return self
    
    def inspect(self, fn: Callable[[Ok], None]) -> Result[Ok, Err]:
        fn(self.unwrap())
        return self
    
    def expect_err(self, msg: str) -> Err:
        raise Panic(msg)

    def is_ok_and(self, fn: Callable[[Ok], bool]) -> bool:
        return fn(self.unwrap())

    def flatten(self) -> Result[Ok, Err]:
        assert isinstance(self.unwrap(), Result)
        return self.unwrap()

    def iter(self) -> Iterator[Ok]:
        return iter([self.unwrap()])
    
    def err(self) -> Option[Err]:
        return none()
    
    def is_err_and(self, fn: Callable[[Err], bool]) -> bool:
        return False
    
    def map_or(self, default: R, fn: Callable[[Ok], R]) -> R:
        return fn(self.unwrap())

    def map_or_else(self, default: Callable[[Err], R], fn: Callable[[Ok], R]) -> R:
        return fn(self.unwrap())
    
    def or_else(self, fn: Callable[[Err], Result[Ok, R]]) -> Result[Ok, R]:
        return self

class err(Result[Ok, Err]):
    def __init__(self, value: Err):
        self.T = value

    def __str__(self):
        return f'Result.err({self.unwrap_err()!r})'
    
    def __repr__(self):
        return str(self)

    def __eq__(self, another):
        return isinstance(another, self.__class__) and self.unwrap_err() == another.unwrap_err()

    def unwrap(self) -> NoReturn:
        _panic(self.T, "called .unwrap() on err")

    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]:
        return self

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True
    
    def unwrap_err(self) -> Err:
        return self.T

    def expect(self, msg: str) -> Ok:
        _panic(self.T, msg)

    def ok(self) -> Option[Ok]:
        return none()

    def unwrap_or(self, default: Ok) -> Ok:
        return default
    
    def unwrap_or_else(self, fn: Callable[[Err], Ok]) -> Ok:
        return fn(self.unwrap_err())

    def map_err(self, fn: Callable[[Err], R]) -> Result[Ok, R]:
        return err(fn(self.unwrap_err()))
    
    def inspect_err(self, fn: Callable[[Err], None]) -> Result[Ok, Err]:
        fn(self.unwrap_err())
        return self
    
    def inspect(self, fn: Callable[[Ok], None]) -> Result[Ok, Err]:
        return self
    
    def expect_err(self, msg: str) -> Err:
        return self.unwrap_err()

    def is_ok_and(self, fn: Callable[[Ok], bool]) -> bool:
        return False

    def flatten(self) -> Result[Ok, Err]:
        return self

    def iter(self) -> Iterator[Ok]:
        return iter([])
    
    def err(self) -> Option[Err]:
        return some(self.unwrap_err())

    def is_err_and(self, fn: Callable[[Err], bool]) -> bool:
        return fn(self.unwrap_err())

    def map_or(self, default: R, fn: Callable[[Ok], R]) -> R:
        return default
    
    def map_or_else(self, default: Callable[[Err], R], fn: Callable[[Ok], R]) -> R:
        return default(self.unwrap_err())
    
    def or_else(self, fn: Callable[[Err], Result[Ok, R]]) -> Result[Ok, R]:
        return fn(self.unwrap_err())

from .option import Option, some, none