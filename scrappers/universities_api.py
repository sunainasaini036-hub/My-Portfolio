import requests


# Universities API URL
API_URL = "http://universities.hipolabs.com/search?country=India"


def get_universities():
    """
    Fetch university data from the Universities API.

    Returns:
        list: List of university records.
    """

    try:

        response = requests.get(API_URL, timeout=10)

        response.raise_for_status()

        universities = response.json()

        return universities

    except requests.exceptions.RequestException as e:

        print(f"Error fetching university data: {e}")

        return []