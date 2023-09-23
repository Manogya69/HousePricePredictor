import mysql.connector

# Replace with your MySQL database connection details
config = {
    "host": "localhost",
    "user": "user",
    "password": "user",
    "database": "housepricepredictor",
}

try:
    # Create a connection to the MySQL database
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as e:
    print(f"Error: {e}")
