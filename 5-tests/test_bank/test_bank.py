import pytest
from bank import value


def test_lower_case():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("what's up?") == 100


def test_upper_case():
    assert value("Hello") == 0
    assert value("Hey") == 20


def test_sentence():
    assert value("Hello, sir. How may I help you?") == 0
    assert value("Hey, how are you?") == 20


def test_wrong_type():
    with pytest.raises(AttributeError):
        value(3)
