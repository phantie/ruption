- Implements pacify module
- Implements subset of [Option](https://doc.rust-lang.org/std/option/enum.Option.html) enum 
- Implements subset of [Result](https://doc.rust-lang.org/std/result/enum.Result.html) enum

## Examples:

### Option:
```python
from ruption.option import some
assert (
    some(2)
    .map(lambda x: x * 2)
    .inspect(print) # output: 4
    .unwrap()) == 4
```

### Result:
```python
from ruption.result import ok
assert (
    ok(2)
    .map(lambda x: x * 2)
    .inspect(print) # output: 4
    .unwrap()) == 4
```

### Pacify:
```python
from ruption.pacify import pacify_callable_result
from ruption.pacify import pacify_call_result
from ruption.pacify import pacify_callable
from ruption.pacify import pacify_call

# pacify_callable for Option, pacify_callable_result for Result
@pacify_callable_result()
def div(dividend, divisor):
    return dividend / divisor

assert div(10, 5).is_ok_and(lambda r: r == 2)
assert div(10, 0).is_err_and(lambda e: isinstance(e, ZeroDivisionError))

# pacify_call for Option, pacify_call_result for Result
assert pacify_call(lambda: 2 + 2).contains(4)
```

Imports:

    from ruption.pacify import *
    from ruption.option import Option, some, none
    from ruption.result import Result, ok, err
    from ruption.panic import Panic

    
Installation:
    
    pip install git+https://github.com/phantie/ruption.git


