from http.server import HTTPServer, BaseHTTPRequestHandler
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

from app import App
from dbcon import DbCon
import sys

app = App(DbCon())

class WebLoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('> got:', self.path)
        qs = parse_qs(urlparse(self.path).query)
        if 'msg' in qs:
            msg = qs["msg"][0]
        else:
            msg = None
        if 'src' in qs:
            src = qs["src"][0]
        else:
            src = None
        if msg != None:
            app.send(src, msg)
        self.send_response(204)
        self.end_headers()

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = 80
httpd = HTTPServer(('', int(port)), WebLoggerHandler)
print("httpd starting on :", port)
httpd.serve_forever()
