import http.server
import socketserver
import json

# Specify the port on which your server should listen
PORT = 8080

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        # Print the received data
        print("Received data:")
        print(data)

        # You can process the data and send a response here

        # Respond with a simple message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Data received by the server", 'utf-8'))

# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
