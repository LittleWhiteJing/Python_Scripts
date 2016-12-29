import SocketServer,commands

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
			cmd_status,cmd_result = commands.getstatusoutput(self.data)
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
