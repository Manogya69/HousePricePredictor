import http.server
import json
from database_connection import unique_house_list
from database_connection import image_data

# Global variable to store user preferences
user_preferences = {}


# Function to calculate a score for a house based on the degree of matching with user preferences
def calculate_score(house, user_preferences):
    # Initialize the score
    score = 0

    # Extract user preferences from the dictionary
    house_type_preference = user_preferences.get('houseType')
    house_price_preference = user_preferences.get('housePrice')
    location_preference = user_preferences.get('location')
    selected_amenities = user_preferences.get('selectedAmenities', [])

    # Compare house features with user preferences
    if house_type_preference and house_type_preference == house.get('house_type'):
        score += 1

    if house_price_preference and house_price_preference == house.get('price_range'):
        score += 1

    if location_preference and location_preference == house.get('location'):
        score += 1

    for amenity in selected_amenities:
        if amenity in house and house[amenity]:
            score += 1  # Increase the score for matching amenities

    return score

# Function to filter houses based on user preferences and a minimum matching score threshold
def filter_houses_by_preferences(user_preferences, houses, min_score_threshold=0):
    filtered_houses = []
    for house in houses:
        score = calculate_score(house, user_preferences)
        if score >= min_score_threshold:
            filtered_houses.append(house)
    return filtered_houses
filtered_houses = filter_houses_by_preferences(user_preferences, unique_house_list, min_score_threshold=3)

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    # def do_OPTIONS(self):
    #     self.send_response(200)
    #     self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')  # Replace with your front-end URL
    #     self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    #     self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    #     self.end_headers()
        
    def do_POST(self):
        global user_preferences  # Use the global variable

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_preferences = json.loads(post_data.decode('utf-8'))

        # Print the received data
        print("Received data:")
        print(user_preferences)
        
        # Send a response to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'data received')

    def do_GET(self):
        global user_preferences

        if user_preferences is not None:
            # Calculate scores for each house based on user preferences
            scored_houses = []
            for house in unique_house_list:
                score = calculate_score(house, user_preferences)
                scored_houses.append({"house_id": house["house_id"], "score": score})

            # Sort the houses by their scores in descending order
            scored_houses.sort(key=lambda x: x["score"], reverse=True)

            # Get the top 5 houses with the highest scores
            top_5_houses = scored_houses[:5]

           # Create a JSON response containing the top 5 house IDs
        top_5_house_ids = [house["house_id"] for house in top_5_houses]
        # response_data = {"top_5_houses": top_5_house_ids}
        response_data = {
        "user_preference": user_preferences,
        "top_5_houses": top_5_house_ids,
        "unique_house_list": unique_house_list,
        "house_images_data": image_data
    }

        # Set CORS headers to allow requests from http://localhost:5500
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

if __name__ == '__main__':
    try:
        server = http.server.HTTPServer(('localhost', 8080), MyRequestHandler)
        print('Server started on http://localhost:8080')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped.')
