import requests

def link():
    response=requests.get('http://www.omdbapi.com/?t=the%20matrix&apikey=35b13908').json()
    print(response["Title"])
    print(2020-int(response["Year"]))

link()