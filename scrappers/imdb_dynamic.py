from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_movies():

    options = Options()
    # options.add_argument("--headless=new")   # Uncomment after testing

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.imdb.com/chart/top/")

    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
        )
    )

    movie_cards = driver.find_elements(
        By.CSS_SELECTOR,
        "li.ipc-metadata-list-summary-item"
    )

    movies = []

    for movie in movie_cards:

        # -------------------------
        # Title
        # -------------------------
        try:
            title = movie.find_element(
                By.CSS_SELECTOR,
                "h4"
            ).text
        except:
            title = "N/A"

        # -------------------------
        # Year, Runtime, Certificate
        # -------------------------
        try:
            metadata = movie.find_elements(
                By.CSS_SELECTOR,
                "div.sc-a96da33f-5.emmHuq.cli-title-metadata"
            )

            year = metadata[0].text if len(metadata) > 0 else "N/A"
            duration = metadata[1].text if len(metadata) > 1 else "N/A"
            certificate = metadata[2].text if len(metadata) > 2 else "N/A"

        except:
            year = "N/A"
            duration = "N/A"
            certificate = "N/A"

        # -------------------------
        # Rating
        # -------------------------
        try:
            rating = movie.find_element(
                By.CSS_SELECTOR,
                "span.ipc-rating-star--rating"
            ).text
        except:
            rating = "N/A"

        # -------------------------
        # IMDb Link
        # -------------------------
        try:
            link = movie.find_element(
                By.TAG_NAME,
                "a"
            ).get_attribute("href")
        except:
            link = ""

        # -------------------------
        # Poster Image
        # -------------------------
        try:
            image = movie.find_element(
                By.TAG_NAME,
                "img"
            ).get_attribute("src")
        except:
            image = ""

        movies.append({

            "title": title,
            "year": year,
            "duration": duration,
            "certificate": certificate,
            "rating": rating,
            "link": link,
            "image": image

        })

    driver.quit()

    return movies