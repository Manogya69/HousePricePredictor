import mysql.connector

def fetch_houses_data():
    # Database connection parameters
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "housepricepredictor"
    }

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Define an SQL query to retrieve data from the "houses" table
        query = "SELECT * FROM houses"
        cursor.execute(query)

        # Fetch all rows of the result set
        houses_data = cursor.fetchall()

        return houses_data

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
