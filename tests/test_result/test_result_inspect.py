from imports import *



def test_ok_inspect(capsys):
    ok(1).inspect(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == "1"

def test_err_inspect(capsys):
    err(1).inspect(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == ""


def test_inspect_class_method_form(capsys):
    Result.inspect(ok(1), lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == "1"