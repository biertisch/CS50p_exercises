import pytest
from twttr import shorten


def test_lower_case():
    assert shorten("twitter") == "twttr"


def test_upper_case():
    assert shorten("TWITTER") == "TWTTR"


def test_sentence():
    assert shorten("Banana split") == "Bnn splt"


def test_punctuation():
    assert shorten("Hello, wonderful person!") == "Hll, wndrfl prsn!"


def test_no_vowels():
    assert shorten("1234") == "1234"
    assert shorten("Smprt") == "Smprt"


def test_wrong_type():
    with pytest.raises(TypeError):
        shorten(1)
