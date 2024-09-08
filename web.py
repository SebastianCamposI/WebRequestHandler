from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
        path_parts = self.url().path.strip('/').split('/')
        project = path_parts[1] if len(path_parts) > 1 else 'desconocido'
        web_part = path_parts[2] if len(path_parts) > 2 else 'desconocido'
        
        author = self.query_data().get('autor', 'desconocido')

        return f"""
        <h1>Proyecto: {web_part} Autor: {author}</h1>
        """


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()