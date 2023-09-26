import http.server
import socketserver
import json
from database_connection import fetch_houses_data  # Import the fetch_houses_data function from your database_connection module

# Define the port where the server will listen
PORT = 8080

# Create a custom request handler to handle incoming requests
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        # Set the CORS headers to allow requests from your frontend URL
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')  # Replace with your frontend URL
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')  # Include OPTIONS
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):  # Change from POST to GET for fetching data
        if self.path == '/get_houses':
            # Set the CORS headers for GET requests
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')  # Replace with your frontend URL
            self.end_headers()

            # Fetch data from the database using the fetch_houses_data function
            houses_data = fetch_houses_data()  # Use the imported function to fetch data from the database

            # Convert data to JSON and send it as a response
            self.wfile.write(json.dumps(houses_data).encode())
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
