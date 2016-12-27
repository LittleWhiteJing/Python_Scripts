import socket,time

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
	s.sendall('Hello,DarkBlue!')
	data = s.recv(1024)
	time.sleep(2)
	print 'Received',repr(data)
s.close()
