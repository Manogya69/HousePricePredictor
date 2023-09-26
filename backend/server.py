import http.server
import socketserver
import json

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

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Parse the JSON data received from the client
        try:
            data = json.loads(post_data.decode('utf-8'))
            print("Received data:")
            print(data)
            
            # Modify the response_data to include both the message and the received data
            response_data = {
                "message": "Data received by the server",
                "received_data": data  # Include the received data
            }

            # Set the HTTP status code and send the response data as JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"error": "Invalid JSON data"}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
