""" An attempt to copy official Rust Option API. https://doc.rust-lang.org/std/option/enum.Option.html

    Methods not suitable for python, for ex. whose deal with pointers, refs, etc are not implemented.

    Because None is a reserved word, "Some and None" became "some and none".

    Methods renamed for the same reason:
        and: also
        or: otherwise

    Changed func. signatures:
        unwrap_or_default: added 'type' argument considering python cannot infer type.

"""

from abc import ABC, abstractmethod
from copy import deepcopy

def instancer(cls):
    return cls()

class Option:

    class ValueIsNone(Exception): ...

    class InvalidArgument(Exception): ...

    class noneIsExpected(Exception): ...

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

        @abstractmethod
        def get_or_insert(self, value): ...
        
        @abstractmethod
        def get_or_insert_with(self, f: callable): ...

        # @abstractmethod
        # def take(self): ...

        @abstractmethod
        def zip(self, another): ...

        @abstractmethod
        def zip_with(self, another, f: callable): ...

        @abstractmethod
        def copied(self): ...

        @abstractmethod
        def cloned(self): ...

        @abstractmethod
        def expect_none(self): ...

        @abstractmethod
        def unwrap_none(self): ...

        @abstractmethod
        def unwrap_or_default(self, type): ...

        @abstractmethod
        def flatten(self): ...

    
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

        def get_or_insert(self, value):
            return self

        def get_or_insert_with(self, f):
            return self

        # def take(self):
        #     self_copy = some(self.T)
        #     self = none
        #     return self_copy

        def zip(self, another):
            if isinstance(another, some):
                self.T = (self.T, another.T)
                return self
            else:
                return none

        def zip_with(self, another, f):
            if isinstance(another, some):
                self.T = f(self.T, another.T)
                return self
            else:
                return none

        def copied(self):
            return some(self.T)

        # basically the same behaviour 
        # as you get from copied. but slower.
        def cloned(self):
            return deepcopy(self)

        def expect_none(self):
            raise Option.noneIsExpected('actual value is ' + str(self))

        def unwrap_none(self): 
            raise self.expect_none()

        def unwrap_or_default(self, type):
            return self.unwrap()

        def flatten(self):
            return self.T

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

        def get_or_insert(self, value):
            return some(value)

        def get_or_insert_with(self, f):
            return some(f())

        # def take(self):
        #     return self

        def zip(self, another):
            return self

        def zip_with(self, another, f):
            return self

        def copied(self):
            return self

        def cloned(self):
            return self

        def expect_none(self): ...

        def unwrap_none(self):
            return self

        def unwrap_or_default(self, type):
            return type()

        def flatten(self):
            return self

some, none = Option.some, Option.none

