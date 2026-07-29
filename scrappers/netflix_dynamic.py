from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_netflix():

    options = Options()
    options.add_argument("--start-maximized")

    # Uncomment after testing
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    url = "https://www.netflix.com/tudum/top10"

    driver.get(url)

    wait = WebDriverWait(driver, 30)

    wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "table tbody tr")
        )
    )

    time.sleep(5)

    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    print("Rows Found :", len(rows))

    netflix_data = []

    for row in rows:

        # -----------------------------
        # Rank
        # -----------------------------

        try:
            rank = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-title"] .rank'
            ).text.strip()
        except:
            rank = "N/A"

        # -----------------------------
        # Title
        # -----------------------------

        try:
            title = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-title"] button'
            ).text.strip()
        except:
            title = "N/A"

        # -----------------------------
        # Poster
        # -----------------------------

        try:
            poster = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-title"] img'
            ).get_attribute("src")
        except:
            poster = ""

        # -----------------------------
        # Weeks
        # -----------------------------

        try:
            weeks = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-weeks"]'
            ).text.strip()
        except:
            weeks = "N/A"

        # -----------------------------
        # Views
        # -----------------------------

        try:
            views = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-views"]'
            ).text.strip()
        except:
            views = "N/A"

        # -----------------------------
        # Runtime
        # -----------------------------

        try:
            runtime = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-runtime"]'
            ).text.strip()
        except:
            runtime = ""

        # -----------------------------
        # Hours
        # -----------------------------

        try:
            hours = row.find_element(
                By.CSS_SELECTOR,
                '[data-uia="top10-table-row-hours"]'
            ).text.strip()
        except:
            hours = ""

        netflix_data.append({

            "rank": rank,
            "title": title,
            "poster": poster,
            "weeks": weeks,
            "views": views,
            "runtime": runtime,
            "hours": hours,
            "link": "https://www.netflix.com/tudum/top10"

        })

    driver.quit()

    return netflix_data


if __name__ == "__main__":

    movies = get_netflix()

    print("\nTotal Movies :", len(movies))

    for movie in movies:

        print("-" * 60)

        print("Rank     :", movie["rank"])
        print("Title    :", movie["title"])
        print("Weeks    :", movie["weeks"])
        print("Views    :", movie["views"])
        print("Runtime  :", movie["runtime"])
        print("Hours    :", movie["hours"])
        print("Poster   :", movie["poster"])
        print("Link     :", movie["link"])