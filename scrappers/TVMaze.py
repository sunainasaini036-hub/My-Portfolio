import requests
import pandas as pd
def get_shows():
    url = "https://api.tvmaze.com/shows"
    response = requests.get(url)
    return response.json()