from ruption.result import ok



assert (
    ok(2)
    .map(lambda x: x * 2)
    .inspect(print) # output: 4
    .unwrap()) == 4


