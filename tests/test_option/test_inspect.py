from imports import *



def test_some_inspect(capsys):
    some(1).inspect(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == "1"

def test_err_inspect(capsys):
    none().inspect(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == ""

