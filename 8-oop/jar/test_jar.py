from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3
    with pytest.raises(ValueError):
        jar3 = Jar(-1)
    with pytest.raises(TypeError):
        jar4 = Jar("10")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar(5)
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar1.deposit(1)
    jar2 = Jar(5)
    with pytest.raises(ValueError):
        jar2.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(4)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.withdraw(2)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
