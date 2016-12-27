import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		# self.request is the TCP socket connected to the client
		while 1:
			self.data = self.request.recv(1024).strip()
			if not self.data: break
			print "{} wrote:".format(self.client_address[0])
			print self.data
			# just send back the same data,but upper-cased
			self.request.sendall(self.data.upper())

if __name__ == '__main__':

	HOST,PORT = "localhost",9999

	# create the server,binding to localhost on port 9999
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
	
	# Activate the server; this will keep running until you 
	# interrupt the program with Ctrl+c
	server.serve_forever()
