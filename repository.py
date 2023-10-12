import models
import connection


def get_london_houses(query: str):
    conn = connection.ConnectionSingleton.get_connection()

    cursor = conn.cursor()
    cursor.execute(query)

    data = cursor.fetchall()

    return [models.House.from_data(item=item) for item in data]
