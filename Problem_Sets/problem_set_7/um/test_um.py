from um import count

def test_beginning():
    assert count("yum yum") == 0
    assert count("um yum") == 1
    assert count(" um ") == 1

def test_case():
    assert count("UM Um um") == 3
    assert count("um Um Um") == 3
    assert count("num yUM UM uM") == 2

def test_punctuation():
    assert count("um.........") == 1
    assert count("um...um") == 2
    assert count("um.um") == 2
    assert count("umumum clumsy rum") == 0

def test_count():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") ==1
    assert count("Um, thanks, um...") == 2





