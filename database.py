import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="kia_store_locator",
)

cursor = connection.cursor()

def insert_dealer_urls(dealer_urls):

    sql = """
    INSERT INTO dealer_urls (state_name, city_name, url)
    VALUES (%s, %s, %s)
    """

    values = []

    for dealer in dealer_urls:
        values.append(
            (
                dealer.get("state"),
                dealer.get("city"),
                dealer.get("url"),
            )
        )

    cursor.executemany(sql, values)

    connection.commit()

    print(f"{cursor.rowcount} dealer URLs inserted.")
    
def insert_locations(locations):

    sql = """
    INSERT INTO location_outlet (url, address, state_name, city_name, phone_number, email)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = []

    for location in locations:

        values.append(
            (
                location.get("url"),
                location.get("address"),
                location.get("state_name"),
                location.get("city_name"),
                location.get("phone_number"),
                location.get("email"),
            )
        )

    cursor.executemany(sql, values)

    connection.commit()

    print(f"{cursor.rowcount} rows inserted.")


def close_connection():
    cursor.close()
    connection.close()
