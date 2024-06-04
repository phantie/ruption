

from typing import Callable, TypeVar
import functools
from .option import some, none, Option
from .result import ok, err, Result, Err

__all__ = [
    "pacify_call",
    "pacify_callable",
    "pacify_call_result",
    "pacify_callable_result",
]


R = TypeVar('R')

def log_fn(e) -> None:
    global logger
    try:
        logger
    except NameError:
        ...
    else:
        logger.exception(f"Swallowed: {e}")

def pacify_call(fn: Callable[[], R], *, log = True, log_fn = log_fn) -> Option[R]:
    try:
        return some(fn())
    except Exception as e:
        if log:
            log_fn(e)
        return none()


def pacify_callable(
    log: bool = True,
    log_fn: Callable[[Exception], None] = log_fn) \
    -> Callable[[Callable[..., R]], Callable[..., Option[R]]]:

    def pacify_callable(func: Callable[..., R]) -> Callable[..., Option[R]]:
        """Protects function call from any exception popping,
        On success returns function result wrapped in some
        On exception returns none"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Option[R]:
            return pacify_call(lambda: func(*args, **kwargs), log = log, log_fn = log_fn)
        return wrapper
    return pacify_callable


def pacify_call_result(fn: Callable[[], R]) -> Result[R, Err]:
    try:
        return ok(fn())
    except Exception as e:
        return err(e)


def pacify_callable_result() \
    -> Callable[[Callable[..., R]], Callable[..., Result[R, Err]]]:

    def pacify_callable_result(func: Callable[..., R]) -> Callable[..., Result[R, Err]]:
        """Protects function call from any exception popping,
        On success returns function result wrapped in ok
        On exception returns error wrapped in err"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Result[R, Err]:
            return pacify_call_result(lambda: func(*args, **kwargs))
        return wrapper
    return pacify_callable_result

