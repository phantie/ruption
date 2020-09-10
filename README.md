# rust_option
Implementation of Rusts Option Enum in python. https://doc.rust-lang.org/std/option/enum.Option.html
A step towards writing more reliable sofware in python.

Methods not suitable for python, for ex. whose which deal with pointers, refs, etc are not implemented.

Because None is a reserved word, "Some and None" became "some and none".

Methods renamed for the same reason:

    and: also / _and
    or: otherwise / _or

Changed func. signatures:

    unwrap_or_default: added 'type' argument considering python cannot infer type
    zip: not one required argument but unlimited amount of arguments
    zip_with: unlimited amount of positional arguments, and required kwonly argument 'f'

Preferred usage:

from option.prelude import *
