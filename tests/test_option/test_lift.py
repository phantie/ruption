from ruption import *

def test_lift():
    def addOne(x):
        return x + 1

    addOneToOption = Option.lift(addOne)

    assert addOneToOption(some(1)) == some(2)