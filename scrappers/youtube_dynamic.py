from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_videos():

    options = Options()

    options.add_argument("--start-maximized")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0 Safari/537.36"
    )

    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.youtube.com/results?search_query=trending+videos")

    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "ytd-video-renderer")
        )
    )

    # Scroll to load more videos

    for _ in range(8):

        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);"
        )

        time.sleep(2)

    videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")

    print("Videos Found:", len(videos))

    all_videos = []

    seen = set()

    for video in videos:

        try:

            title_element = video.find_element(
                By.CSS_SELECTOR,
                "a#video-title"
            )

            title = title_element.text.strip()

            link = title_element.get_attribute("href")

            if not title or title in seen:
                continue

            seen.add(title)

        except:
            continue

        # Thumbnail

        try:

            img = video.find_element(By.CSS_SELECTOR, "img")

            image = (
                img.get_attribute("src")
                or img.get_attribute("data-thumb")
                or img.get_attribute("data-src")
                or img.get_attribute("data-lazy-src")
                or ""
            )

        except:
            image = ""

        # Channel

        try:

            channel = video.find_element(
                By.CSS_SELECTOR,
                "#channel-name a"
            ).text.strip()

        except:
            channel = "N/A"

        # Views

        try:

            metadata = video.find_elements(
                By.CSS_SELECTOR,
                "#metadata-line span"
            )

            views = metadata[0].text if len(metadata) > 0 else "N/A"

        except:
            views = "N/A"

        # Duration

        try:

            duration = video.find_element(
                By.CSS_SELECTOR,
                "span.ytd-thumbnail-overlay-time-status-renderer"
            ).text.strip()

        except:
            duration = "N/A"

        all_videos.append({

            "title": title,
            "image": image,
            "channel": channel,
            "views": views,
            "duration": duration,
            "link": link

        })

        if len(all_videos) == 20:
            break

    driver.quit()

    return all_videos


if __name__ == "__main__":

    videos = get_videos()

    print("Total:", len(videos))

    for video in videos:
        print(video)