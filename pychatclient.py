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
import threading
import sys
import time

threadLock = threading.Lock()
chatOn = True

def receiving(nameOfThread, socketLink):
    while chatOn:
        try:
            threadLock.acquire()
            while True:
                data, addr = socketLink.recvfrom(4096)
                print str(data)
        except:
            pass
        finally:
            threadLock.release()

def sending_data(socketLink, server):
    name = raw_input("Name: ")
    message = raw_input(name + " -> ")

    while message != "QUIT":
        if message != "":
            socketLink.sendto(name + ": " + message, server)
        threadLock.acquire()
        message = raw_input(name + "-> ")
        threadLock.release()
        time.sleep(0.2)
    chatOn = False

def main():
    client_host = socket.gethostbyname(socket.gethostname())
    client_port = 0
    try:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        server = (server_host, server_port)

        socketLink = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketLink.bind((client_host,client_port))
        socketLink.setblocking(0)

        recvThread = threading.Thread(target=receiving, args=("RecvThread", socketLink))
        recvThread.start()

        sending_data(socketLink, server)

        recvThread.join()
        socketLink.close()

    except:
        print "USAGE: ./pychatclient.py <SERVER_IP> <SERVER_PORT>"
        print "Exiting.."


if __name__ == '__main__':
    main()
