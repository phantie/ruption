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


