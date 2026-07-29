from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_movies():

    options = Options()

    # Uncomment this when deploying
    # options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:

        driver.get("https://www.imdb.com/chart/top/")

        wait = WebDriverWait(driver, 20)

        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "h4.ipc-title__text")
            )
        )

        movie_cards = driver.find_elements(
            By.CSS_SELECTOR,
            "li.ipc-metadata-list-summary-item"
        )

        movies = []

        for movie in movie_cards:

            # -----------------------
            # Title
            # -----------------------
            try:
                title = movie.find_element(
                    By.CSS_SELECTOR,
                    "h4.ipc-title__text"
                ).text
            except:
                title = "N/A"

            # -----------------------
            # Rating
            # -----------------------
            try:
                rating = movie.find_element(
                    By.CSS_SELECTOR,
                    ".ipc-rating-star--rating"
                ).text
            except:
                rating = "N/A"

            # -----------------------
            # Metadata
            # -----------------------
            year = "N/A"
            duration = "N/A"
            certificate = "N/A"

            try:
                metadata = movie.find_elements(
                    By.CSS_SELECTOR,
                    "span.cli-title-metadata-item"
                )

                if len(metadata) >= 1:
                    year = metadata[0].text

                if len(metadata) >= 2:
                    duration = metadata[1].text

                if len(metadata) >= 3:
                    certificate = metadata[2].text

            except:
                pass

            # -----------------------
            # Movie Link
            # -----------------------
            try:
                link = movie.find_element(
                    By.TAG_NAME,
                    "a"
                ).get_attribute("href")
            except:
                link = ""

            # -----------------------
            # Poster
            # -----------------------
            try:
                image = movie.find_element(
                    By.TAG_NAME,
                    "img"
                ).get_attribute("src")
            except:
                image = ""

            movies.append(
                {
                    "title": title,
                    "rating": rating,
                    "year": year,
                    "duration": duration,
                    "certificate": certificate,
                    "link": link,
                    "image": image,
                }
            )

        return movies

    finally:
        driver.quit()