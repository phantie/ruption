from imports import *



def test_ok_inspect_err(capsys):
    ok(VALUE).inspect_err(lambda e: ...)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_err_inspect_err(capsys):
    err(1).inspect_err(lambda e: print(e, end = ""))
    captured = capsys.readouterr()
    assert captured.out == "1"

def test_inspect_err_class_method_form(capsys):
    Result.inspect_err(ok(VALUE), (lambda e: ...))
    captured = capsys.readouterr()
    assert captured.out == ""