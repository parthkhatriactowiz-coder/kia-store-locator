from parsel import Selector


def parse_cities(states_file):
    html = states_file.read_text(encoding="utf-8")
    selector = Selector(text=html)

    locations = []

    stores = selector.xpath('//div[@class="panel panel-default custom-panel"]')

    for store in stores:

        branch = (
            store.xpath('.//p[contains(@class,"city-main-sub-title")]/text()')
            .get(default="")
            .strip()
        )

        address = (
            store.xpath('.//p[contains(@class,"grey-text")][1]/text()')
            .get(default="")
            .strip()
        )

        delivery_time = (
            store.xpath('.//p[contains(@class,"red-text")]/text()')
            .get(default="")
            .strip()
        )

        cost = (
            store.xpath('.//div[contains(@class,"res-cost")]//span[last()]/text()')
            .get(default="")
            .strip()
        )

        hours = (
            store.xpath(
                './/div[contains(@class,"res-timing")]//div[contains(@class,"search-grid-right-text")]/text()[1]'
            )
            .get(default="")
            .strip()
        )

        status = (
            store.xpath(
                './/div[contains(@class,"res-timing")]//span[contains(@class,"green")]/text()'
            )
            .get(default="")
            .strip()
        )

        good_for = (
            store.xpath('.//div[contains(@class,"clearfix")]//p[@class="mb-0"]/text()')
            .get(default="")
            .strip()
        )

        store_url = store.xpath(
            '(//div[contains(@class, "media-body")]/a/@href)[1]'
        ).get()
        phone = (
            store.xpath(
                './/div[contains(@class,"modal-body")]/p[contains(@class,"zred")]/text()'
            )
            .get(default="")
            .strip()
        )

        locations.append(
            {
                "branch": branch,
                "address": address,
                "delivery_time": delivery_time,
                "cost": cost,
                "hours": hours,
                "status": status,
                "good_for": good_for,
                "phone": phone,
                "store_url": "https://www.dominos.co.in" + store_url,
            }
        )

    return locations
