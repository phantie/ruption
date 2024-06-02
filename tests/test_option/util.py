# value used in some(VALUE) tests to not think about
VALUE = 42

# value not equal to VALUE of the same type
OTHER_VALUE = 13

# value of different type to VALUE
OTHER_TYPE_VALUE = 3.14

assert VALUE != OTHER_VALUE

# type of VALUE
VALUE_TYPE = int

# type not of VALUE
OTHER_TYPE = float

assert VALUE_TYPE is not OTHER_TYPE

assert type(VALUE) is VALUE_TYPE
assert type(OTHER_TYPE_VALUE) is OTHER_TYPE

# value used in some(VALUE) type hint snippets
TYPE_HINT_VALUE = 42