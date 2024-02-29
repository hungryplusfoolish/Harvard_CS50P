import pytest
from numb3rs import validate

def test_length():
    assert validate("100.0.00000.0") == False
    assert validate("100.100.100.100") == True
    assert validate("1.2.3.4") == True

def test_values():
    assert validate("755.100.100.100") == False
    assert validate("155.100.100.100") == True
    assert validate("55.99.256.100") == False




