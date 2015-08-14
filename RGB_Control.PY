import serial
import time
ser = serial.Serial('/dev/ttyAMA0', 9600,timeout=1)
#ser = serial.Serial("COM5", baudrate = 9600, timeout = 2)

end=0x11
for nvl in range(0x00,0xff):
	sal=[0x28,0x00,0x00,end,0x0C,nvl,0x00]
    #s=[0x28,0x00,0x00,end,0x0C,0,0x00]
	tmp="out ";
	sal[2]=len(sal)
	chk=0
	for k in range(0,len(sal)-1):
		chk+=sal[k]
		#print(k)
		#chk=chk-0x3a
	chk=chk%0x100
	sal[len(sal)-1]=chk
	print(format(sal[len(sal)-1],'02x'))
	for k in sal:
		tmp+=':'+format(k,'02x')
	#s[(s[2]-1)]=s[(s[2]-1)]/2
	#intput()
	print(tmp)
	sid=""
	for j in sal:
		sid+=chr(j)
	
	ser.write(sid)
out=ser.read(50)


p=":".join("{:02x}".format(ord(c)) for c in out)

print("rcv "+p)

#input()