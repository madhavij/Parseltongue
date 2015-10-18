# The MIT License (MIT)
#
# Copyright (c) 2015 Anshul Joshi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import socket
import time
import sys

def chatserver(server_host, server_port):
    connected_clients = []

    socketLink = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketLink.bind((server_host, server_port))
    socketLink.setblocking(0)

    serving = True

    while serving:
        try:
            data, addr = socketLink.recvfrom(4096)
            if addr not in connected_clients:
                connected_clients.append(addr)
            print "TimeStamp: " + time.ctime(time.time()) + str(addr) + ": : " + str(data)
            for client in connected_clients:
                socketLink.sendto(data, client)
        except:
            pass

    socketLink.close()


def main():
    server_host = socket.gethostbyname(socket.gethostname())
    try:
        server_port = int(sys.argv[1])
    except:
        print "No port given or unable to open Parseltongue on given server port."
        print "Opening Parseltongue on port 24100 instead."
        server_port = 24100

    print "Parseltongue - Chat server starting......."
    print "Server IP: " + str(server_host)
    print "Server Host: " + str(server_port) + "\n"
    chatserver(server_host, server_port)


if __name__ == '__main__':
    main()
