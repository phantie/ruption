import ruption
import ruption.result
from ruption.result import *

print(
    list(
        map(Result.unwrap,
        filter(
            Result.is_ok,
        
            [ok(123), err(-12)]
        )
        )
    )
)