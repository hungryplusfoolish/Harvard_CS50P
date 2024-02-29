from working import convert
import pytest


def test_wrong_input():
    with pytest.raises(ValueError):
        assert convert("cat") == ValueError

    with pytest.raises(ValueError):
        assert convert("9 ZM to 10 PM") == ValueError

    with pytest.raises(ValueError):
        assert convert("10:01 AM to 11 ") == ValueError

    with pytest.raises(ValueError):
        assert convert("9:72 to 6:30")


def test_minutes():
    assert convert("10:31 AM to 11:55 AM") == "10:31 to 11:55"
    assert convert("9:09 AM to 10:09 PM") == "09:09 to 22:09"
    assert convert("12:01 AM to 12:01 PM") == "00:01 to 12:01"

def test_hours():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1 AM to 12 PM") == "01:00 to 12:00"
    assert convert("2 AM to 12 PM") == "02:00 to 12:00"

def test_outofrange():
    with pytest.raises(ValueError):
        convert("16:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("-1:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("11:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("6:92 to 6:30")
