from http.server import HTTPServer, BaseHTTPRequestHandler
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

import psycopg2

class DbCon:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user = "oejdfpyizarfhm",
                                               password = "fb4b18b8a9ba59b6720ab50bb230175466630d71aafa1f7a9463ed47e8e69d5a",
                                               host = "ec2-54-197-254-189.compute-1.amazonaws.com",
                                               port = "5432",
                                               database = "d4vvkr2us65lvp")

            self.cursor = self.connection.cursor()
            print("connected to - ",
                  self.execSql("Select version();").result(),"\n")

        except (Exception, psycopg2.Error) as error :
            print ("error:", error)
            self.__del__()

    def execSql(self, sql='Select version();'):
            self.cursor.execute("Select version();")
            return self
    def result(self):
        return self.cursor.fetchone()
    def __del__(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("connection closed")

class WebLoggerHandler(BaseHTTPRequestHandler):
    def __init__():
        self.dbcon = DbCon()
    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)
        msg = qs["msg"]
        print('> got:', msg)
        self.dbcon.execSql("insert into messages (msg, created_at) values ('%s', '%s');" % (msg[0], '2020-01-22'))
        self.send_response(204)
        self.end_headers()

httpd = HTTPServer(('0.0.0.0', 18473), WebLoggerHandler)
httpd.serve_forever()
