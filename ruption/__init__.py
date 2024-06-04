"""
Implementation of Rusts Option Enum in python. https://doc.rust-lang.org/std/option/enum.Option.html .
A step towards writing more reliable software in python.

Methods not suitable for python, regarding pointers, immutability, etc - are not implemented.

Due to "None" being reserved, "Some and None" are renamed to "some and none".
    
Install:
    
    pip install git+https://github.com/phantie/ruption.git -U

Import:

    from ruption import Option, some, none, Panic
"""

from .panic import Panic
from .option import *
from .result import *

__all__ = ['Panic', 'Option', 'some', 'none', 'Result', 'ok', 'err']
__version__ = 1, 4, 1

