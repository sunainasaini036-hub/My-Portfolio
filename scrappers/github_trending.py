from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_repositories():

    options = Options()
    options.add_argument("--start-maximized")

    # Uncomment after testing
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    driver.get("https://github.com/trending")

    wait = WebDriverWait(driver,20)

    wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR,"article.Box-row")
        )
    )

    repositories = driver.find_elements(
        By.CSS_SELECTOR,
        "article.Box-row"
    )

    data=[]

    for repo in repositories:

        try:
            title = repo.find_element(
                By.CSS_SELECTOR,
                "h2 a"
            ).text.replace("\n","").replace(" ","")
        except:
            title="N/A"

        try:
            link = repo.find_element(
                By.CSS_SELECTOR,
                "h2 a"
            ).get_attribute("href")
        except:
            link=""

        try:
            description = repo.find_element(
                By.CSS_SELECTOR,
                "p"
            ).text
        except:
            description="No description available."

        try:
            language = repo.find_element(
                By.CSS_SELECTOR,
                "[itemprop='programmingLanguage']"
            ).text
        except:
            language="N/A"

        try:
            stars = repo.find_elements(
                By.CSS_SELECTOR,
                "a.Link--muted"
            )[0].text
        except:
            stars="N/A"

        try:
            forks = repo.find_elements(
                By.CSS_SELECTOR,
                "a.Link--muted"
            )[1].text
        except:
            forks="N/A"

        data.append({

            "title":title,
            "description":description,
            "language":language,
            "stars":stars,
            "forks":forks,
            "link":link

        })

    driver.quit()

    return data


if __name__=="__main__":

    repos=get_repositories()

    print("Repositories:",len(repos))

    for repo in repos:

        print(repo)