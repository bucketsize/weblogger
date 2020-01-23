import socket
import sys

class UDPC:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data, ipaddr='127.0.0.1', port=53743):
        self.s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20) # Change TTL (=20) to suit
        self.s.sendto(bytes(data, 'utf8'), (ipaddr, port))

UDPC().send(sys.argv[1])
