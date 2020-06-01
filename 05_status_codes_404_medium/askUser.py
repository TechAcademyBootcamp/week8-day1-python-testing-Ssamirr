import requests

page=input("Enter link: ")
response = requests.get(page)
if response.status_code == 200:
    print("200 success")
    exit()
print("404 not found")
