import threading
import serial
connected=False
port='/dev/ttyAMA0'
baud=9600
serial_port=serial.Serial(port,baud,timeout=0)

def handle_data(data):
	print(data)
def read_from_port(ser):
	global connected
	while not connected:
		connected=True
		while True:
			print("teste")
			reading=ser.readline().decode()
			handle_data(reading)
thread=threading.Thread(target=read_from_port,args=(serial_port,))
thread.start()
