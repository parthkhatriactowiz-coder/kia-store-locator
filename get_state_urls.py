import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import json


def get_state_urls(url, headers):
    session = requests.Session()

    retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])

    session.mount("https://", HTTPAdapter(max_retries=retries))
    session.mount("http://", HTTPAdapter(max_retries=retries))

    response = session.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()

    base_url = "https://www.kia.com/in/buy/find-a-dealer/result.html"

    dealer_urls = []

    for state in data.get("data", {}).get("stateAndCity", []):

        state_key = state["val1"]["key"]
        state_name = state["val1"]["value"]

        for city in state.get("val2", []):

            city_key = city["key"]
            city_name = city["value"]

            dealer_url = f"{base_url}?state={state_key}&city={city_key}"

            dealer_urls.append(
                {"state": state_name, "city": city_name, "url": dealer_url}
            )


    with open("dealer_urls.json", "w", encoding="utf-8") as f:
        json.dump(dealer_urls, f, indent=4, ensure_ascii=False)

    return dealer_urls
