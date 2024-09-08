from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.handle_home()
        else:
            self.handle_404()

    def handle_home(self):
        try:
            # Lee el contenido del archivo home.html
            with open('home.html', 'r') as file:
                content = file.read()
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            self.handle_404()

    def handle_404(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <head><title>404 Not Found</title></head>
        <body>
        <h1>404 Not Found</h1>
        <p>The requested URL was not found on this server.</p>
        </body>
        </html>
        """)

if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()