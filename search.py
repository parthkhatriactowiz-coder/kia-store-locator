import os
import requests
from pathlib import Path


def do_search(domain_api_url, state, headers):

    url = f"{domain_api_url}{state}"

    os.makedirs("states", exist_ok=True)

    filename = os.path.basename(state) + ".html"
    file_path = Path("states") / filename

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    file_path.write_text(response.text, encoding="utf-8")


    return file_path
