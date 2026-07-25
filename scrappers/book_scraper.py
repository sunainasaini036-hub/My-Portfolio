from bs4 import BeautifulSoup
import requests

url = "https://www.goodreads.com/quotes"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def book_data():
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    all_books = []
    # Find all quote cards
    quotes = soup.find_all("div", class_="quote")
    print("Quotes Found:", len(quotes))
    for book in quotes:
        title = book.find("span", class_="authorOrTitle")
        quote = book.find("div", class_="quoteText")
        likes = book.find("a", class_="smallText")
        # Find author image
        image = book.find("img")
        image_url = image.get("src", "") if image else ""
        all_books.append({
            "Title": title.get_text(strip=True) if title else "N/A",
            "Quote": quote.get_text(" ", strip=True) if quote else "N/A",
            "Likes": likes.get_text(strip=True) if likes else "N/A",
            "Image": image_url
        })
    return all_books