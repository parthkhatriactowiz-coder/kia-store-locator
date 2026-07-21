def parse_cities(states_json):
    base_url = "https://www.kia.com/in/buy/find-a-dealer/result.html"
    locations = []

    for data in states_json:

        address = f"{data.get('address1', '')} {data.get('address2', '')}".strip()

        locations.append(
            {
                "url": f'{base_url}?state={data["stateCode"]}&city={data["cityCode"]}',
                "address": address,
                "state_name": data.get("stateName", ""),
                "city_name": data.get("cityName", ""),
                "phone_number": data.get("phone1", ""),
                "email": data.get("email", ""),
            }
        )

    return locations
