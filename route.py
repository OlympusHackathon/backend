# from http.server import BaseHTTPRequestHandler, HTTPServer


# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/html')
#         self.end_headers()

#         message = "Hello, World! Here is a GET response"
#         self.wfile.write(bytes(message, "utf8"))
#     def do_POST(self):
#         self.send_response(200)
        # self.send_header('Content-type','multipart/form-data')
        # self.end_headers()

#         message = "Hello, World! Here is a POST response"
#         self.wfile.write(bytes(message, "utf8"))


#     def do_POST_text(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/html')
#         self.end_headers()

#         content_length = int(self.headers['Content-Length'])
#         post_data = self.rfile.read(content_length).decode('utf-8')
       

#         response_data = f"Received POST data: {post_data}"
        
#         self.wfile.write(response_data.encode('utf-8'))

# # with HTTPServer(('', 8000), handler) as server:
# #     server.serve_forever()
        
#     def run_server(server_class=HTTPServer, handler_class=MyRequestHandler, port=8800):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print(f'Starting server on port {port}...')
#     httpd.serve_forever()

# # Run the server
# run_server()


from http.server import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        response_data = post_data
        
        self.wfile.write(response_data.encode('utf-8'))
    
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/hello':
            self.send_response(200, "Text")
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(b'Text received and saved successfully')

        else:
            self.send_response(200, "PDF")
            self.send_header('Content-type','multipart/form-data')
            self.end_headers()
    
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
        
            with open('received_pdf.pdf', 'wb') as f:
                f.write(post_data)
        
            self.wfile.write(b'PDF file received and saved successfully')

def run_server(server_class=HTTPServer, handler_class=MyRequestHandler, port=8800):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

run_server()
