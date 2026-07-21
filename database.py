import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="kia_store_locator",
)

cursor = connection.cursor()


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
