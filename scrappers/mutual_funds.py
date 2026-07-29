from bs4 import BeautifulSoup
import requests

url = "https://finance.yahoo.com/markets/mutualfunds/top/"
response = requests.get(url)


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_data():
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    data = []
    rows = soup.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        data.append([col.get_text(strip=True) for col in cols])
    return data