import pytest
from fuel import convert
from fuel import gauge


def test_format():
    with pytest.raises(ValueError):
        convert("cat")

    with pytest.raises(ValueError):
        convert("1/2/3")


def test_integer():
    with pytest.raises(ValueError):
        convert("dog/2")

    with pytest.raises(ValueError):
        convert("8/cat")

    with pytest.raises(ValueError):
        convert("dog/cat")


def test_max():
    with pytest.raises(ValueError):
        convert("5/4")


def test_negative():
    with pytest.raises(ValueError):
        convert("3/-4")

    with pytest.raises(ValueError):
        convert("-3/4")


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_valid():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("5/5") == 100
    assert convert("0/5") == 0


def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"


def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"


def test_percentage():
    assert gauge(75) == "75%"
    assert gauge(8) == "8%"


def test_wrong_types():
    with pytest.raises(AttributeError):
        convert(0.7)

    with pytest.raises(TypeError):
        gauge("90")
