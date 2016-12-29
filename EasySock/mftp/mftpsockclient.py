import socket,sys

HOST,PORT = "localhost",9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to server and send data
sock.connect((HOST,PORT))

while 1:
	cmd = raw_input("Your command:").strip()
	if len(cmd) == 0: continue
	sock.sendall(cmd+"\n")
	
	if cmd.split()[0] == 'get':
		print "Getting the file..."
		with open(cmd.split()[1],'wb') as f:
			while 1:
				data = sock.recv(1024)
				if data == 'FileTransferDone': break
				f.write(data)
		print "Finished!"
		continue
	else:			
		# Receive data from the server and shut down
		received = sock.recv(1024)
		print received

sock.close()
