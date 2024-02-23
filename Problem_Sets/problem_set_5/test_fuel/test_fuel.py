from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("99/100") == 99
    assert convert("0/50") == 0
    assert convert("3/4") == 75


def test_guage():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"

def test_zero_div():
    with pytest.raises(ValueError):
        convert("cat/10")
    with pytest.raises(ZeroDivisionError):
        convert("50/0")
