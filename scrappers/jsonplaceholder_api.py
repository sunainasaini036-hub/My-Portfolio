import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    response = requests.get(URL)
    data = response.json()
    return data