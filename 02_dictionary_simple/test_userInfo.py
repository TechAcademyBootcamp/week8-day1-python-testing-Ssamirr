from userInfo import userInfo

def test_info():
    user_info = {
    "first_name": "Elon",
    "last_name": "Musk"
    }
    expected="Elon Musk"
    actual=userInfo(user_info)
    assert expected == actual