import threading
import serial
import queue

rcv_data=queue.Queue(maxsize=0)

def rcv_data(ser,q):
	while True:
		c=ser.read()
		q.put(c)
		q.task_done()
		

