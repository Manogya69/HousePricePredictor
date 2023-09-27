import http.server
import json
from database_connection import unique_house_list

# Global variable to store user preferences
user_preferences = None

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        global user_preferences  # Use the global variable

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_preferences = json.loads(post_data.decode('utf-8'))

        # Print the received data
        # print("Received data:")
        # print(user_preferences)

    def do_GET(self):
        global user_preferences

        # Print the unique houses when a GET request is made
        print("Unique Houses:")
        for house in unique_house_list:
            print(house)

if __name__ == '__main__':
    try:
        server = http.server.HTTPServer(('localhost', 8080), MyRequestHandler)
        print('Server started on http://localhost:8080')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped.')
