import threading
import serial
import Queue
import sys
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 2)
data_rcv=Queue.Queue()


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

	
def enviar_cmd(cmd):
	GPIO.output(18,1)
	#time.sleep(0.1)
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
	time.sleep(0.05)
	GPIO.output(18,0)


def rcv_data(ser,q):
	while True:
		d=ser.read(64)
		if(len(d)>0):
			q.put(d)
			#print("rcv>",d)
		#q.task_done()
	
def handle_data(q):
	while True:	
		data=q.get()
		q.task_done()
		tmp="\n"
		for k in data:
			tmp+=":"+format(ord(k),'02x')
			#tmp+=":"+str(k)
		print(tmp)

tRcv=threading.Thread(target=rcv_data,args=(ser,data_rcv,))
tHandle=threading.Thread(target=handle_data,args=(data_rcv,))
tRcv.daemon=True
tHandle.daemon=True
tRcv.start()
tHandle.start()

end=int(sys.argv[1],0)
tp=int(sys.argv[2],0)
comandos=[0x00]*(len(sys.argv)-3)
		
for y in range(3, len(sys.argv)):
	comandos[y-3]=int(sys.argv[y],0)
	
enviar_cmd(cmdo(end,tp,comandos))
newcmd=""
while newcmd!='0':
	newcmd=raw_input("Digite um novo Comando ou 0 para sair:")
	c=newcmd.split(' ')
	if len(c)>1:
		end=int(c[0],0)
		tp=int(c[1],0)
		comandos=[0x00]*(len(c)-2)
		for y in range(2,len(c)):
			comandos[y-2]=int(c[y],0)
		enviar_cmd(cmdo(end,tp,comandos))
	#print(newcmd)
	#print(c)
