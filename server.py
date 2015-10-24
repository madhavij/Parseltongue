import socket, select

def broadcast(sock,message):
	for socket in connectionList:
		if socket!=serverSocket and socket !=sock:
			try:
				socket.send(message)
			except:
				socket.close()
				connectionList.remove(socket)

if __name__=="__main__":

	connectionList= []
	recvBuffer    = 4096
	port          = 5000

	serverSocket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	serverSocket.bind(("0.0.0.0",port))
	serverSocket.listen(10)

	connectionList.append(serverSocket)

	print "Chat server started on port: "+str(port)

	while 1:
		readSocket,writeSocket,errorSocket=select.select(connectionList,[],[])

		for sock in readSocket:
			if sock==serverSocket:
				sockobj,address=serverSocket.accept()
				connectionList.append(sockobj)
				print "Client (%s, %s) connected" %address

				broadcast(sockobj,"[%s:%s] entered chatroom\n" %address )
			else:
				try:
					data=sock.recv(recvBuffer)
					if data:
						broadcast(sock,"\r"+'<'+str(sock.getpeername())+'>'+data)
				except:
					broadcast(sock,"Client (%s, %s) is offline" %address)
					print "Client (%s,%s) is offline" %address
					sock.close()
					connectionList.remove(sock)
					continue

	serverSocket.close()
