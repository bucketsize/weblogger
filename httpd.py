from http.server import HTTPServer, BaseHTTPRequestHandler
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

from app import App
from dbcon import DbCon

app = App(DbCon())

class WebLoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('> got:', self.path)
        qs = parse_qs(urlparse(self.path).query)
        msg = qs["msg"][0]
        src = qs["src"][0]
        app.send(src, msg)
        self.send_response(204)
        self.end_headers()

httpd = HTTPServer(('0.0.0.0', 18473), WebLoggerHandler)
httpd.serve_forever()
