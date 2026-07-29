import requests
import pandas as pd

url = "https://fakestoreapi.com/products"

def get_products():
    response = requests.get(url)
    data = response.json()
    return data