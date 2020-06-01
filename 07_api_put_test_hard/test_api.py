import requests

def test_blog():
    put_data={
    "full_name": "Idris Blogger"
    }
    response = requests.put("http://35.225.243.133/bloggers/1/",data=put_data)  
    expected_status_code = 200
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = put_data["full_name"]
    actual_title = data["full_name"]
    assert expected_title == actual_title

def test_blog_error1():
    put_data={
    "full_name": "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd "
    }
    response = requests.put("http://35.225.243.133/bloggers/1/",data=put_data)  
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = ["Ensure this field has no more than 180 characters."]
    actual_title = data["full_name"]
    assert expected_title == actual_title

def test_blog_error2():
    put_data={}
    response = requests.put("http://35.225.243.133/bloggers/1/",data=put_data)  
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = ["This field is required."]
    actual_title = data["full_name"]
    assert expected_title == actual_title

def test_blog_error3():
    put_data={
    "id": 1223
    }
    response = requests.put("http://35.225.243.133/bloggers/1/",data=put_data)  
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = ["This field is required."]
    actual_title = data["full_name"]
    assert expected_title == actual_title