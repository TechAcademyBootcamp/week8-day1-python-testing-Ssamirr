import requests

def test_blog():
    post_data={
    "full_name": "Idris Shabanli"
    }
    response = requests.post("http://35.225.243.133/bloggers/",data=post_data)  
    expected_status_code = 201
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = post_data["full_name"]
    actual_title = data["full_name"]
    assert expected_title == actual_title


def test_blog_error():
    post_data={
    "full_name": "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd "
    }
    response = requests.post("http://35.225.243.133/bloggers/",data=post_data)  
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = ["Ensure this field has no more than 180 characters."]
    actual_title = data["full_name"]
    assert expected_title == actual_title

def test_blog_error2():
    post_data={}
    response = requests.post("http://35.225.243.133/bloggers/",data=post_data)  
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = ["This field is required."]
    actual_title = data["full_name"]
    assert expected_title == actual_title

def test_blog_error3():
    post_data={
        "id": 1223
    }
    response = requests.post("http://35.225.243.133/bloggers/",data=post_data)  
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()

    expected_title = ["This field is required."]
    actual_title = data["full_name"]
    assert expected_title == actual_title