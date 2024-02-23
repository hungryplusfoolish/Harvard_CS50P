from plates import is_valid

def test_num():
    assert is_valid("0") == False
    assert is_valid("-10") == False
    assert is_valid("10") == False

def test_punc():
    assert is_valid(",") == False
    assert is_valid("....") == False
    assert is_valid("pla.e") == False

def test_spce():
    assert is_valid("  ") == False
    assert is_valid("      .") == False
    assert is_valid(" howdy     ") == False
