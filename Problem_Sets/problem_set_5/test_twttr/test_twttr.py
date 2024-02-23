from twttr import shorten
import pytest

def test_str():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

def test_punc():
    assert shorten("twitt..er") == "twtt..r"
    assert shorten("TWITT..ER") =="TWTT..R"

def test_int():
    assert shorten("twitt3r") == "twtt3r"
    assert shorten("TWITT3R") == "TWTT3R"
