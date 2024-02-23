from bank import value
import pytest

def test_punc():
    assert value("Hello,") == 0
    assert value("hello ") == 0

def test_int():
    assert value("10") == 100
    assert value ("1") == 100

def test_zero():
    assert value("0") == 100

def test_negative():
    assert value("-10") == 100
    assert value("1") == 100

    