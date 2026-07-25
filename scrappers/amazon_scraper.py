from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/s?k=laptop"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


def amazon_scraper_data():
    response = requests.get(url, headers=HEADERS)
    print("Status Code:", response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    products = []
    product_cards = soup.find_all("div", {"data-component-type": "s-search-result"})
    print("Products Found:", len(product_cards))
   
    for product in product_cards:
        title = product.find("h2")
        price = product.find("span", class_="a-price-whole")
        rating = product.find("span", class_="a-icon-alt")
        image = product.select_one("img.s-image")
        products.append({
            "Title": title.get_text(strip=True) if title else "N/A",
            "Price": price.get_text(strip=True) if price else "N/A",
            "Rating": rating.get_text(strip=True) if rating else "N/A",
          "Image": image["src"] if image else ""
        })
    return products