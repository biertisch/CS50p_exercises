import pytest
from plates import is_valid


def test_length():
    assert is_valid("t") == False
    assert is_valid("ab123456") == False
    assert is_valid("CS55") == True


def test_start():
    assert is_valid("12abc") == False
    assert is_valid("1a23") == False
    assert is_valid("a123") == False
    assert is_valid("ab12") == True


def test_non_alnum():
    assert is_valid("ab!12") == False
    assert is_valid("ab 12") == False
    assert is_valid("ab.12") == False


def test_numbers():
    assert is_valid("ab12cd") == False
    assert is_valid("abc01") == False
    assert is_valid("you739") == True


def test_valid():
    assert is_valid("AbC123") == True
    assert is_valid("HH576") == True
    assert is_valid("FIFTY") == True
    assert is_valid("cs50") == True


def test_wrong_type():
    with pytest.raises(TypeError):
        is_valid(50)
