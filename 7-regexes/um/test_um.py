from um import count


def test_basic():
    assert count("hello, um, world") == 1
    assert count("hello, um, my, um, dear friend") == 2
    assert count("Let me um think about this,um, big, um, problem") == 3


def test_extremities():
    assert count("um...") == 1
    assert count("um?") == 1
    assert count("I'd say um") == 1


def test_case():
    assert count("Um... very interesting") == 1
    assert count("HOW DARE UM YOU") == 1


def test_words_containg_um():
    assert count("That is yummi!") == 0
    assert count("yum") == 0
