import serial

ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 2)

while True:
	dado=ser.read(64)
	if(len(dado)>0):
			p=":".join("{:02x}".format(ord(c)) for c in dado)
			print "rcv "+p
