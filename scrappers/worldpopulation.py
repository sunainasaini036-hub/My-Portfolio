from bs4 import BeautifulSoup
import requests

url = "https://www.worldometers.info/world-population/population-by-country/"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_population_data():
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    rows = soup.find_all("tr")

    for row in rows:

        cols = row.find_all("td")

        if cols:          # Skip empty rows

            data.append([col.get_text(strip=True) for col in cols])

    return data