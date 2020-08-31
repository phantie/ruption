""" An attempt to copy official Rust Option API. https://doc.rust-lang.org/std/option/enum.Option.html

    Methods not suitable for python, for ex. whose deal with pointers, refs, etc are not implemented.

    Because None is a reserved word, "Some and None" became "some and none".

    Methods renamed for the same reason:
        and: also
        or: otherwise

"""

from abc import ABC, abstractmethod


def instancer(cls):
    return cls()

class Option:

    class ValueIsNone(Exception):
        pass


    # wraps/converts any type to Option. None becomes Option.none, Other becomes Option.some(Other)
    @classmethod
    def into(cls, value):
        if value is None:
            return cls.none
        else:
            return cls.some(value)

    class OptionInterface(ABC):
        @abstractmethod
        def unwrap(self): ...

        @abstractmethod
        def unwrap_or(self, another): ...

        @classmethod
        @abstractmethod
        def is_none(self): ...

        @classmethod
        @abstractmethod
        def is_some(self): ...

        @abstractmethod
        def contains(self, value): ...

        @abstractmethod
        def unwrap_or_else(self, f: callable): ...

        @abstractmethod
        def map(self, f: callable): ...

        @abstractmethod
        def map_or(self, default, f: callable): ...

        @abstractmethod
        def map_or_else(self, default: callable, f: callable): ...

        @abstractmethod
        def iter(self) -> iter: ...

        # 'and' is a reserved word. so it use 'also' instead
        @abstractmethod
        def also(self): ...

        @abstractmethod
        def and_then(self, f: callable): ...

        @abstractmethod
        def filter(self, P: callable): ...

        @abstractmethod
        def otherwise(self, another): ...
        
        @abstractmethod
        def or_else(self, f: callable): ...

        @abstractmethod
        def xor(self, optb): ...

    class some(OptionInterface):
        def __init__(self, T):
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
            self.T = f(self.T)
            return self

        def map_or(self, default, f):
            return self.map(f)

        def map_or_else(self, default, f):
            return self.map(f)

        def iter(self):
            return iter([self.T])

        def also(self, another):
            return another

        def and_then(self, f):
            self.T = f(self.T)
            if self.T is none:
                return none

            return self

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


    @instancer
    class none(OptionInterface):
        def __str__(self):
            return 'Option.none'

        def __repr__(self):
            return str(self)

        def unwrap(self):
            raise Option.ValueIsNone

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
            return another is None or self is another

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

some, none = Option.some, Option.none