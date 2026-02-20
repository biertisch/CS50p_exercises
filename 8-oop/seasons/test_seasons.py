from seasons import minutes_since_birth
import pytest

def test_date_format():
    assert minutes_since_birth("2026-02-19") == "Zero minutes"
    assert minutes_since_birth("2025-02-19") == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_since_birth("2024-02-19") == "One million, fifty-two thousand, six hundred forty minutes"
    with pytest.raises(Exception):
        minutes_since_birth("19 February 2026")
    with pytest.raises(Exception):
        minutes_since_birth("19-02-2026")
    with pytest.raises(Exception):
        minutes_since_birth("2026-2-19")
    with pytest.raises(Exception):
        minutes_since_birth("2026/02/19")


def test_value_range():
    with pytest.raises(Exception):
        minutes_since_birth("2020-30-08")
    with pytest.raises(Exception):
        minutes_since_birth("2020-03-32")
    with pytest.raises(Exception):
        minutes_since_birth("0-03-08")
