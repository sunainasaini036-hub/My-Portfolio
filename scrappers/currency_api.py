import requests

def get_currency():

    url = "https://api.frankfurter.app/latest?from=USD&to=INR,EUR,GBP,JPY,AUD,CAD"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {
        "base": "USD",
        "date": "",
        "rates": {}
    }