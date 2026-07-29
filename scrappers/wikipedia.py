from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/Albert_Einstein"


HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/139 Safari/537.36"
}



def wikipedia_scraper_data():

    response = requests.get(
        url,
        headers=HEADERS
    )


    print("Status Code:", response.status_code)


    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )


    wikipedia_data = []


    # -----------------------------
    # Title Extraction
    # -----------------------------

    title = soup.find("h1")


    wikipedia_data.append({

        "Type": "Title",

        "Content":
        title.get_text(strip=True)
        if title else "N/A"

    })



    # -----------------------------
    # Article Paragraphs
    # -----------------------------

    paragraphs = soup.find_all("p")


    for para in paragraphs[:10]:

        text = para.get_text(strip=True)


        if text:

            wikipedia_data.append({

                "Type": "Paragraph",

                "Content": text

            })



    # -----------------------------
    # Headings Extraction
    # -----------------------------

    headings = soup.find_all(
        ["h2","h3"]
    )


    for heading in headings:

        wikipedia_data.append({

            "Type": "Heading",

            "Content":
            heading.get_text(strip=True)

        })



    # -----------------------------
    # Infobox Extraction
    # -----------------------------

    infobox = soup.find(
        "table",
        class_=lambda x: x and "infobox" in x
    )


    if infobox:


        rows = infobox.find_all("tr")


        for row in rows:


            cells = row.find_all(
                ["th","td"]
            )


            if len(cells) == 2:

                wikipedia_data.append({

                    "Type":
                    cells[0].get_text(strip=True),


                    "Content":
                    cells[1].get_text(strip=True)

                })



    # -----------------------------
    # Wikipedia Tables
    # -----------------------------

    tables = soup.find_all("table")


    print(
        "Tables Found:",
        len(tables)
    )


    if tables:


        for row in tables[-1].find_all("tr"):


            cells = row.find_all(
                ["th","td"]
            )


            row_data = []


            for cell in cells:

                row_data.append(
                    cell.get_text(strip=True)
                )


            if row_data:

                wikipedia_data.append({

                    "Type":
                    "Table Row",


                    "Content":
                    " | ".join(row_data)

                })



    print(
        "Data Extracted:",
        len(wikipedia_data)
    )


    return wikipedia_data