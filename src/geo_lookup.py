import requests
from functools import lru_cache


@lru_cache(maxsize=1000)
def get_country(ip):

    try:

        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)

        data = response.json()

        return data.get("country", "Unknown")

    except:

        return "Unknown"
