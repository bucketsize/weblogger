from http.server import HTTPServer, BaseHTTPRequestHandler
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

import psycopg2
from datetime import datetime
import socket

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
                  self.send("Select version();").result(),"\n")

        except (Exception, psycopg2.Error) as error :
            print ("error:", error)
            self.close()

    def send(self, sql='Select version();'):
            print('sql> ', sql)
            self.cursor.execute(sql)
            self.connection.commit()
            return self
    def status(self):
        return self.cursor.statusmessage
    def result(self):
        return self.cursor.fetchone()
    def results(self):
        return self.cursor.fetchall()
    def close(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("connection closed")

dbCon = DbCon()
class WebLoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('> got:', self.path)
        qs = parse_qs(urlparse(self.path).query)
        msg = qs["msg"]
        src = qs["src"]
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
        result = dbCon.send("""
            insert into messages (src, msg, ts_cre)
            values ('%s', '%s', '%s');
            """ % (src[0], msg[0], date_time)).status()
        print(result)
        self.send_response(204)
        self.end_headers()

httpd = HTTPServer(('0.0.0.0', 18473), WebLoggerHandler)
httpd.serve_forever()

class UDPSocket:
    def __init__(ip='127.0.0.1', port=53743):
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.bind((ip, port))
        print('UDPSocket started on %s:%i' % (ip, port))

    def recv(self):
        while True:
            data, addr = sock.recvfrom(1024)
            print("received: ", data)

UDPSpcker().recv()
