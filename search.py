import json
import requests
from pathlib import Path


def do_search(domain_api_url, payload, headers):

    state_code = payload.get("state", "unknown")
    city_code = payload.get("city", "unknown")

    folder_path = Path("states")
    folder_path.mkdir(exist_ok=True)

    file_path = folder_path / f"{state_code}_{city_code}.json"

    response = requests.post(
        domain_api_url,
        headers=headers,
        data=payload,
    )

    response.raise_for_status()

    data = response.json()

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return data["data"]
