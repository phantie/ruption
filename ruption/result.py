
from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import Callable, Any, Iterator, Generic, Union, Tuple, Type, NoReturn, Literal

from .typing import *
from .panic import Panic

__all__ = ['Result', 'ok', 'err']

from typing import NewType, Callable, TypeVar, Any

Ok = TypeVar("Ok")
Err = TypeVar("Err")
R = TypeVar("R")

class Result(Generic[Ok, Err], metaclass=ABCMeta):
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap
    @abstractmethod
    def unwrap(self) -> Ok: ...

    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.map
    @abstractmethod
    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]: ...


class ok(Result[Ok, Err]):
    def __init__(self, value: Ok):
        self.T = value

    def unwrap(self) -> Ok:
        return self.T
    
    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]:
        return ok(fn(self.unwrap()))

class err(Result[Ok, Err]):
    def __init__(self, value: Err):
        self.T = value

    def unwrap(self) -> NoReturn:
        raise Panic(self.T)

    def map(self, fn: Callable[[Ok], R]) -> Result[R, Err]:
        return self