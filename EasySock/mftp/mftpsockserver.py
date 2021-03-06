import SocketServer,commands
import time

class MyTCPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		# self.request is the TCP socket connected to the client
		while 1:
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print "Client %s has logged out!" % self.client_address[0]
				break
			print "{} wrote:".format(self.client_address[0])
			print self.data
			user_input = self.data.split()
			if user_input[0] == 'get':
				print "Starting..."
				with open(user_input[1],'rb') as f:
					self.request.sendall(f.read())
					print "Sending..."			
				time.sleep(0.5)
				self.request.sendall("FileTransferDone")
				continue
			cmd_status,cmd_result =  commands.getstatusoutput(self.data)
			if len(cmd_result.strip()) != 0:
				self.request.sendall(cmd_result)
			else:
				self.request.sendall("Done!")

if __name__ == '__main__':

	HOST,PORT = "localhost",9999

	# create the server,binding to localhost on port 9999
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
	
	# Activate the server; this will keep running until you 
	# interrupt the program with Ctrl+c
	server.serve_forever()
