from ruption import *
from util import VALUE

def test_ok_inspect_err(capsys):
    ok(VALUE).inspect_err(lambda e: ...)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_err_inspect_err(capsys):
    err(1).inspect_err(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == "1"