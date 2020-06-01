from add import add

def test_add():
    given=1
    expected = 2
    actual = add(given)
    assert expected == actual