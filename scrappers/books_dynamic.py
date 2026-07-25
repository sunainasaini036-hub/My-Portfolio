from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
import time


def get_books():

    options = Options()

    # Uncomment while testing if you want to see the browser
    # options.add_argument("--start-maximized")

    # Run in background
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    base_url = "https://books.toscrape.com/"

    driver.get(base_url)

    all_books = []

    page = 1

    while True:

        print(f"Scraping Page {page}")

        time.sleep(1)

        books = driver.find_elements(
            By.CLASS_NAME,
            "product_pod"
        )

        for book in books:

            # -------------------------
            # Title
            # -------------------------

            try:

                title = book.find_element(
                    By.TAG_NAME,
                    "a"
                ).get_attribute("title")

            except:

                title = "N/A"

            # -------------------------
            # Price
            # -------------------------

            try:

                price = book.find_element(
                    By.CLASS_NAME,
                    "price_color"
                ).text

            except:

                price = "N/A"

            # -------------------------
            # Availability
            # -------------------------

            try:

                availability = book.find_element(
                    By.CLASS_NAME,
                    "instock"
                ).text.strip()

            except:

                availability = "N/A"

            # -------------------------
            # Rating
            # -------------------------

            try:

                rating = book.find_element(
                    By.CLASS_NAME,
                    "star-rating"
                ).get_attribute("class").split()[-1]

            except:

                rating = "N/A"

            # -------------------------
            # Image
            # -------------------------

            try:

                image = book.find_element(
                    By.TAG_NAME,
                    "img"
                ).get_attribute("src")

            except:

                image = ""

            # -------------------------
            # Book Link
            # -------------------------

            try:

                link = book.find_element(
                    By.TAG_NAME,
                    "a"
                ).get_attribute("href")

            except:

                link = "#"

            all_books.append({

                "id": len(all_books) + 1,
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "image": image,
                "link": link

            })

        # -------------------------
        # Next Page
        # -------------------------

        try:

            next_button = driver.find_element(
                By.CSS_SELECTOR,
                "li.next a"
            )

            next_url = urljoin(driver.current_url, next_button.get_attribute("href"))

            driver.get(next_url)

            page += 1

        except:

            print("Finished Scraping.")

            break

    driver.quit()

    return all_books


if __name__ == "__main__":

    books = get_books()

    print(f"\nTotal Books : {len(books)}")

    for book in books[:5]:

        print(book)