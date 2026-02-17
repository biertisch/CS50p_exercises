import pytest
from working import convert

def test_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 6 PM") == "10:00 to 18:00"
    assert convert("3:15 PM to 2:30 AM") == "15:15 to 02:30"
    assert convert("7 AM to 12:30 PM") == "07:00 to 12:30"
    with pytest.raises(ValueError):
        convert("9.30 AM to 5.15 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to dusk")
    with pytest.raises(ValueError):
        convert("I work from 9 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("cat")


def test_values():
    with pytest.raises(ValueError):
        convert("A:00 AM to 5:P0 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 2:00 PM")
    with pytest.raises(ValueError):
        convert("3:00 PM to 0:00 AM")
    with pytest.raises(ValueError):
        convert("4:00 PM to 12:60 AM")
    with pytest.raises(ValueError):
        convert("-3:00 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("38:00 AM to 1:00 PM")


def test_conversion():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("5:00 AM to 9:00 PM") == "05:00 to 21:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
