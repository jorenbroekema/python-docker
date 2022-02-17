from functools import partial
import http.server
import socketserver

PORT = 8080
DIRECTORY = "public"

Handler = partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    try:
        httpd.serve_forever()
    except Exception:
        httpd.shutdown()
