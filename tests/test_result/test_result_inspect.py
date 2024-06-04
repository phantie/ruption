from ruption import *
from util import VALUE

def test_ok_inspect(capsys):
    ok(1).inspect(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == "1"

def test_err_inspect(capsys):
    err(1).inspect(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == ""