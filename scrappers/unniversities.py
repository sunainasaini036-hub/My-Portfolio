import requests
import pandas as pd

url ="http://universities.hipolabs.com/search?country=India"

response=requests.get(url)
data = response.json()  