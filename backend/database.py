# import http.server
# import json
# from database_connection import fetch_houses_data, fetch_house_images_data

# # Define global variables to store the retrieved data
# houses_data = []
# house_images_data = []

# # Fetch and store data from the database when the server starts
# houses_data = fetch_houses_data()
# house_images_data = fetch_house_images_data()

# class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/get_merged_data':
#             # Set CORS headers for GET requests
#             self.send_response(200)
#             self.send_header('Content-Type', 'application/json')
#             self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')
#             self.end_headers()

#             # Merge data based on house_id
#             merged_data = []

#             for house in houses_data:
#                 house_id = house[0]
#                 images_for_house = [img for img in house_images_data if img[2] == house_id]
#                 image_urls = [img[3] for img in images_for_house]

#                 house_data_with_images = {
#                     "house_id": house[0],
#                     "house_name": house[1],
#                     "images": image_urls
#                 }

#                 merged_data.append(house_data_with_images)

#             # Convert data to JSON and send it as a response
#             self.wfile.write(json.dumps(merged_data).encode())
#         else:
#             return http.server.SimpleHTTPRequestHandler.do_GET(self)

# # Start the server
# if __name__ == '__main__':
#     try:
#         server = http.server.HTTPServer(('localhost', 8000), MyRequestHandler)
#         print('Server started on http://localhost:8000')
#         server.serve_forever()
#     except KeyboardInterrupt:
#         print('Server stopped.')
