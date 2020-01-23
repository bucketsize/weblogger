import socket

from app import App
from dbcon import DbCon

app = App(DbCon())

class UDPD:
    def __init__(self, ip='', port=53743):
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
        print('UDPSocket started on %s:%i' % (ip, port))
    def recv(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            print("received: ", data)
            app.send("", str(data, 'utf8'))

UDPD().recv()
