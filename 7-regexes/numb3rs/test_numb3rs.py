from numb3rs import validate


def test_pattern():
    assert validate("127.0.0.1") == True
    assert validate("cat") == False
    assert validate("127.0.0") == False
    assert validate("127.0.0.1.2") == False
    assert validate("127.0.0.1.") == False
    assert validate("127..0.1") == False


def test_leading_zeros():
    assert validate("192.64.0.2") == True
    assert validate("192.064.0.2") == False
    assert validate("192.64.0.02") == False
    assert validate("192.64.000.2") == False


def test_integer():
    assert validate("33.20.0.9") == True
    assert validate("33.a.0.9") == False
    assert validate("33.20.0.9c") == False


def test_range():
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.256") == False
    assert validate("45.0.1000.3") == False
    assert validate("-3.18.178.1") == False
