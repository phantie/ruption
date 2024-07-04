

from typing import Callable, TypeVar, ParamSpec
import functools
from .option import some, none, Option
from .result import ok, err, Result, Err
from .panic import Panic

__all__ = [
    "pacify_call",
    "pacify_callable",
    "pacify_call_result",
    "pacify_callable_result",
]


R = TypeVar('R')
P = ParamSpec("P")

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
    except Panic:
        # only Panics and BaseExceptions not get caught
        raise
    except Exception as e:
        if log:
            log_fn(e)
        return none()


def pacify_callable(
    log: bool = True,
    log_fn: Callable[[Exception], None] = log_fn) \
    -> Callable[[Callable[P, R]], Callable[P, Option[R]]]:

    def pacify_callable(func: Callable[P, R]) -> Callable[P, Option[R]]:
        """Protects function call from any exception popping,
        On success returns function result wrapped in some
        On exception returns none"""

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Option[R]:
            return pacify_call(lambda: func(*args, **kwargs), log = log, log_fn = log_fn)
        return wrapper
    return pacify_callable


def pacify_call_result(fn: Callable[[], R]) -> Result[R, Err]:
    try:
        return ok(fn())
    except Panic:
        # only Panics and BaseExceptions not get caught
        raise
    except Exception as e:
        return err(e)


def pacify_callable_result() \
    -> Callable[[Callable[P, R]], Callable[P, Result[R, Err]]]:

    def pacify_callable_result(func: Callable[P, R]) -> Callable[P, Result[R, Err]]:
        """Protects function call from any exception popping,
        On success returns fun/ction result wrapped in ok
        On exception returns error wrapped in err"""

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[R, Err]:
            return pacify_call_result(lambda: func(*args, **kwargs))
        return wrapper
    return pacify_callable_result

