import mysql.connector

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "housepricepredictor"
}

def fetch_houses_data():
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

def fetch_house_images_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Define an SQL query to retrieve data from the "house_images" table
        query = "SELECT * FROM house_images"
        cursor.execute(query)

        # Fetch all rows of the result set
        house_images_data = cursor.fetchall()

        return house_images_data

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetch_data_from_database():
    # Fetch house data from the database using the fetch_houses_data function
    houses_data = fetch_houses_data()

    # Define an empty list to store the converted dictionaries
    houses_data_as_dicts = []

    # Iterate through the rows in houses_data
    for row in houses_data:
        house_dict = {
            "house_id": row[0],
            "house_name": row[1],
            "house_description": row[2],
            "house_type": row[3],
            "price_range": row[4],
            "location": row[5],
            "has_pool": row[6],
            "has_gym": row[7],
            "has_fireplace": row[8],
            "has_yard": row[9],
            "has_garage": row[10],
        }

        # Append the house_dict to the list
        houses_data_as_dicts.append(house_dict)

    return houses_data_as_dicts

def create_unique_house_list(houses_data_as_dicts):
    # Define an empty list to store unique house dictionaries
    house_list = []

    # Iterate through houses_data_as_dicts to create a list of unique houses
    for house_dict in houses_data_as_dicts:
        if house_dict not in house_list:
            house_list.append(house_dict)

    return house_list

# Fetch data for house images
def fetch_house_images():
    # Fetch house images data from the database using the fetch_house_images_data function
    house_images_data = fetch_house_images_data()

    # Define an empty list to store the house image data as dictionaries
    house_images_data_list = []

    # Iterate through the rows in house_images_data
    for row in house_images_data:
        # Assuming the row contains image data, you can create a dictionary to store it
        image_dict = {
            "image_id": row[0],
            "image_name": row[1],
            "house_id": row[2],  
            "image_url": row[3], 
        }

        # Append the image_dict to the list
        house_images_data_list.append(image_dict)

    return house_images_data_list

# Example usage:
house_images_data = fetch_house_images()

# Print the fetched house images data in the console
for image_data in house_images_data:
    print(image_data)

# Fetch data from the database and create a unique house list
unique_house_list = create_unique_house_list(fetch_data_from_database())

# Print the unique house list in the console
for house in unique_house_list:
    print(house)
