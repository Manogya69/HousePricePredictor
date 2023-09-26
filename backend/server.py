import http.server
import socketserver
import json

# Define the port where the server will listen
PORT = 8080

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        # Print the received data
        print("Received data:")
        print(data)

        

        # Process the data here (e.g., prepare it for your algorithm)
        # You can also send a response back to the client based on the processed data













# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
