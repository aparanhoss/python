import serial
import time
import sys
import RPi.GPIO as GPIO
import threading

#ser = serial.Serial('/dev/ttyAMA0', 9600,timeout=1)
ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 2)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


#sal=[0x28,0x00,0x00,end,0x0C,0xff,0x00]
"""
j=0

for arg in sys.argv: 
    print(" - "+arg)
"""
def enviar_cmd(cmd):
	GPIO.output(18,1)
	time.sleep(1)
	chk=0
	cmd[2]=len(cmd)
	for k in range(0,len(cmd)-1):
		chk+=cmd[k]
	chk=chk%0x100
	cmd[len(cmd)-1]=chk
	tmp="out "
	
	for k in cmd:
		tmp+=':'+format(k,'02x')
		ser.write(chr(k))
	print(tmp)
	#time.sleep(1)
	GPIO.output(18,0)


def cmdo(add,cmd,params):
	#data = [0x00] * (6+len(params))
	if(isinstance(params, list)):
		data = [0x00] * (6+len(params))
		j=5
		for pos in params:
			data[j]=pos
			j=j+1
	elif(params is None):
		data = [0x00] * (6)
	else:
		data = [0x00] * (7)
		data[5]=params
	
	data[0]=0x28
	data[3]=add
	data[4]=cmd	
	#data[len(data)]=0x00
	return data
	
def read_from_port(serial):
	while True:
		#print ("teste")
		dado=serial.read(64)
		if(len(dado)>0):
			p=":".join("{:02x}".format(ord(c)) for c in dado)
			print "rcv "+p
	
#enviar_cmd(sal)
#dtmp=cmdo(end,0x0C,0xff)
#enviar_cmd(dtmp)
#enviar_cmd(cmdo(end,0x0C,[0x01,0x02,0x05,0x04]))
#enviar_cmd(cmdo(end,int(sys.argv[1],0),int(sys.argv[2],0)))

#entradas terminal
end=int(sys.argv[1],0)
tp=int(sys.argv[2],0)
comandos=[0x00]*(len(sys.argv)-3)

thread = threading.Thread(target=read_from_port,args=(ser,))
thread.daemon=True
thread.start()

for y in range(3, len(sys.argv)):
	comandos[y-3]=int(sys.argv[y],0)
	
enviar_cmd(cmdo(end,tp,comandos))



#out=ser.read(10)
#p=":".join("{:02x}".format(ord(c)) for c in out)
#print "rcv "+p
input()
#while True:
#    time.sleep(1)