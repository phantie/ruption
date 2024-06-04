
from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import Callable, Any, Iterator, Generic, Union, Tuple, Type, NoReturn, Literal

from .typing import *
from .panic import Panic


__all__ = ['Result', 'ok', 'err', 'Ok', 'Err']

from typing import NewType, Callable, TypeVar, Any

Ok = TypeVar("Ok")
Err = TypeVar("Err")
R = TypeVar("R")

class Result(Generic[Ok, Err], metaclass=ABCMeta):
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap
    @abstractmethod
    def unwrap(self) -> Ok:
        """
            returns inner value if ok
            panics if err
        """


    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.map
    @abstractmethod
    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]: ...
    
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

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap_err
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


class ok(Result[Ok, Err]):
    def __init__(self, value: Ok):
        self.T = value

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

class err(Result[Ok, Err]):
    def __init__(self, value: Err):
        self.T = value

    def unwrap(self) -> NoReturn:
        raise Panic("called .unwrap() on err")

    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]:
        return self

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True
    
    def unwrap_err(self) -> Err:
        return self.T

    def expect(self, msg: str) -> Ok:
        raise Panic(msg)

    def ok(self) -> Option[Ok]:
        return none()

from .option import Option, some, none