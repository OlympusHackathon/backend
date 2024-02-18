from testing import get_chapter_info
from http.server import BaseHTTPRequestHandler, HTTPServer
from ml import summarize
import json
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
            content_length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(content_length).decode('utf-8'))
            summary = summarize(data, 3)
            response_data = {"status": "success", "message":summary}

            self.wfile.write(json.dumps(response_data).encode('utf-8'))

        else:
            self.send_response(200)
            self.send_header('Content-type','multipart/form-data')
            self.end_headers()
    
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            with open('received_pdf.pdf', 'wb') as f:
                f.write(post_data)
        
            parsed_pdf = get_chapter_info()
            response_data = {"status": "success", "message":parsed_pdf, 'img':'https://www.includehelp.com/dbms/Images/document-database.jpg','img2':'https://www.researchgate.net/profile/T-M-K-K-Jinasena/publication/375205522/figure/fig5/AS:11431281202599661@1698933307507/The-database-scheme-of-the-system.ppm'}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run_server(server_class=HTTPServer, handler_class=MyRequestHandler, port=8800):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

run_server()
