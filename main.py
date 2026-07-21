from search import do_search
from parse import parse_cities
from pathlib import Path
from get_state_urls import get_state_urls
import json

BASE_DIR = Path(__file__).resolve().parent
base_url = "https://www.kia.com/api/kia2_in/findAdealer.getStateCity.do"
dominos_headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-length": "0",
    "csrf-token": "undefined",
    "origin": "https://www.kia.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.kia.com/in/buy/find-a-dealer.html",
    "sec-ch-ua": '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "Cookie": "__cflb=04dToPPtdqTVeCCaEkPQCuAY2ttTQ1pF2uQ398sJ3Z; __cf_bm=D4_HILpJJJ0xnL9HcQvB9tU_DZhe0rw_73LonzC_Ohs-1784613664.181504-1.0.1.1-0YRc078odLSVtFwHQdvtdnt3U0jLkP2iezYxkpizNIB.IcCAJwqghW4l3xomHCbcsQC0mY9GWLtM58F4lV34vKbR.j4i4hczSBblJgyNPhKjumVhKpb6790pm6cDRP.A; renderid=rend01; WMONID=VPX-C5rD-Yw; SCOUTER=z1u3ilsoir2gih; _gid=GA1.2.1989283538.1784613665; cookie-agree=true; _gat_UA-137890001-2=1; JSESSIONID=node01knj92mvxlq9g1v3g7g92rxs8g1093916.node0; _gcl_au=1.1.1869757788.1784613665.477724822.1784613753.1784613752.1005465289.1784613665.1784613795; _ga_9PSV9LG5D2=GS2.1.s1784613665$o1$g1$t1784613795$j5$l0$h0; _ga=GA1.1.377233924.1784613665; _uetsid=8fea48c084c911f19c42c1df2c700a50; _uetvid=8fea6f2084c911f1a4ddb1d75cb6bdc2",
}


def main():
    states = get_state_urls(url=base_url, headers=dominos_headers)

    all_locations = []

    #     cities = do_search(
    #         domain_api_url="https://www.dominos.co.in",
    #         state=state["store_link"],
    #         headers=dominos_headers,
    #     )
    #     locations = parse_cities(cities)

    #     all_locations.extend(locations)

    # output_dir = BASE_DIR / "parsed"
    # output_dir.mkdir(parents=True, exist_ok=True)

    # output_json_path = output_dir / "location_outlet.json"

    # with open(output_json_path, "w", encoding="utf-8") as out_file:
    #     json.dump(all_locations, out_file, indent=4, ensure_ascii=False)

    # print(f"Successfully saved {len(all_locations)} locations.")


if __name__ == "__main__":
    main()
