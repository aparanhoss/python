import socket
import sys
from ac import Ac
class MyServer:
	def __init__(self):
		self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('192.168.0.4', 8000)
		self.conn.bind(self.server_address)
	def listen(self):
		self.conn.listen(1)
		while True:
			print("Espperando ...")
			connection,client=self.conn.accept()
			try:
				print (sys.stderr,'from ',client)
				while True:
					data = connection.recv(16)
					print("recebido %s"%data)
					Arc=Ac("192.168.0.201",4998)
					Arc.open()
					#if data.isnumeric():
					print(type(data))
					Arc.setTemp(int(data))
					Arc.close()
				
			finally:
				connection.close()
				
			