from http.server import BaseHTTPRequestHandler, HTTPServer

# Diccionario con el contenido HTML para cada ruta
contenido = {
    '/': """<html>
<head><title>Home</title></head>
<body>
<h1>Bienvenido a la Página de Inicio</h1>
<ul>
    <li><a href="/proyecto/web-uno">Proyecto Web Uno</a></li>
    <li><a href="/proyecto/web-dos">Proyecto Web Dos</a></li>
    <li><a href="/proyecto/web-tres">Proyecto Web Tres</a></li>
</ul>
</body>
</html>""",
    '/proyecto/web-uno': """<html>
<head><title>Proyecto Web Uno</title></head>
<body>
<h1>Proyecto: web-uno</h1>
</body>
</html>""",
    '/proyecto/web-dos': """<html>
<head><title>Proyecto Web Dos</title></head>
<body>
<h1>Proyecto: web-dos</h1>
</body>
</html>""",
    '/proyecto/web-tres': """<html>
<head><title>Proyecto Web Tres</title></head>
<body>
<h1>Proyecto: web-tres</h1>
</body>
</html>""",
}

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Verifica si la ruta solicitada está en el diccionario de contenido
        if self.path in contenido:
            self.handle_content()
        else:
            self.handle_404()

    def handle_content(self):
        # Obtiene el contenido HTML correspondiente a la ruta
        html_content = contenido.get(self.path, "<html><body><h1>404 Not Found</h1></body></html>")
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

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
