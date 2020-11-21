Implementation of Rusts Option Enum in python. https://doc.rust-lang.org/std/option/enum.Option.html .
A step towards writing more reliable software in python.

Methods not suitable for python, regarding pointers, immutability, etc - ain`t implemented.

Due to "None" being reserved, "Some and None" are renamed to "some and none".

These methods are also renamed:

    and: also / _and
    or: otherwise / _or

Changed func. signatures:

    unwrap_or_default: added 'type' :Type[Any]: argument considering python cannot infer type
    zip: unlimited amount of positional arguments
    zip_with: unlimited amount of positional arguments, and required kw-only argument 'f' :Callable:
    
Install:
    
    pip install git+https://github.com/phantie/ruption.git --upgrade

Preferred usage:

    from ruption import * #includes [Option, some, none, Panic]
