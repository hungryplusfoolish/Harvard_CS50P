from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        assert Jar(14)
        assert Jar(-1)
        assert Jar("cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        assert Jar().deposit(-1)
        assert Jar().deposit("Cat")
        assert Jar().deposit(14)


def test_withdraw():
    with pytest.raises(ValueError):
        assert Jar().deposit(-1)
        assert Jar().deposit("dog")
        assert Jar().deposit(14)