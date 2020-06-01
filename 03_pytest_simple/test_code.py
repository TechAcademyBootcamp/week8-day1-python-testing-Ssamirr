from main import divide

def test_divide1():
    arg1 = 3
    arg2 = 2
    expected = 1.5
    actual = divide(arg1,arg2)
    assert expected == actual

def test_divide2():
    arg1 = 4
    arg2 = 2
    expected = 2.0
    actual = divide(arg1,arg2)
    assert expected == actual

def test_divide3():
    arg1 = 10
    arg2 = 0
    expected = 'You cannot divide 0!'
    actual = divide(arg1,arg2)
    assert expected == actual