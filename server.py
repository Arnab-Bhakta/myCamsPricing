import http.server
import socketserver
import os

web_dir = os.path.join(os.path.dirname(__file__), 'public')
os.chdir(web_dir)

# as per OP comments default is 17995
port = int(os.environ.get('PORT', 17995))
Handler = http.server.SimpleHTTPRequestHandler


def create():
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("server running on *."+str(port))
        httpd.serve_forever()
