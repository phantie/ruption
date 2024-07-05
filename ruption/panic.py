__all__ = ["Panic"]



class Panic(Exception): ...


def _panic(e, msg):
    if isinstance(e, BaseException):
        raise Panic(msg) from e
    else:
        raise Panic(msg)


