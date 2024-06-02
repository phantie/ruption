"""
Implementation of Rusts Option Enum in python. https://doc.rust-lang.org/std/option/enum.Option.html .
A step towards writing more reliable software in python.

Methods not suitable for python, regarding pointers, immutability, etc - are not implemented.

Due to "None" being reserved, "Some and None" are renamed to "some and none".

These methods are also renamed:

    and: also / _and
    or: otherwise / _or

Changed func. signatures:

    unwrap_or_default: added `type` argument because python cannot infer type
    zip: no limits for positional arguments
    zip_with: no limits for positional arguments, and required kw-only callable `f`
    flatten: got `times` argument to flatten an object several times, .flatten(2) == .flatten().flatten()
    
Install:
    
    pip install git+https://github.com/phantie/ruption.git -U

Import:

    from ruption import Option, some, none, Panic
"""

from .panic import Panic
from .option import *

__all__ = ['Panic', 'Option', 'some', 'none']
__version__ = 1, 4, 1

