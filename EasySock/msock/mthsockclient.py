import socket,sys

HOST,PORT = "localhost",9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to server and send data
sock.connect((HOST,PORT))

while 1:
	data = raw_input("Your command:").strip()
	if len(data) == 0: continue
	sock.sendall(data+"\n")

	# Receive data from the server and shut down
	received = sock.recv(1024)

	print "Sent: {}".format(data)
	print "Received: {}".format(received)

sock.close()
