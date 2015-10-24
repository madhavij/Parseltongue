import socket,select,sys,string

def prompt():
	sys.stdout.write('<You>')
	sys.stdout.flush()

if __name__=="__main__":
	
	if(len(sys.argv)<3):
		print 'Usage: python telnet.py hostname post'
		sys.exit()
	host= sys.argv[1]
	port=int(sys.argv[2])

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect((host,port))
	except:
		print 'Unable to connect'
		sys.exit()
	print 'Connected to remote host'
	prompt()
	
	while 1:
		socketList=[sys.stdin,s]
		readSocket,writeSocket,errorSocket=select.select(socketList,[],[])
		for sock in readSocket:
			if sock==s:
				data=sock.recv(4096)
				if not data:
					print 'Disconnected from char server'
					sys.exit()
				else:
					sys.stdout.write(data)
					prompt()
			else:
				msg=sys.stdin.readLine()
				s.send(msg)
				prompt()






























