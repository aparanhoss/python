import threading
import time
import queue

q=queue.Queue()

data=""
is_data=False


def add_data():
	global data
	global is_data
	for j in range(0,5):
		data=data+str(j)
		is_data=True
		time.sleep(0.1)

def print_data():
	global data
	global is_data
	for k in range(0,10):
		if is_data:
			print(data)
			is_data=False
		time.sleep(0.1)
t1=threading.Thread(target=add_data)
t2=threading.Thread(target=print_data)
t1.start()
t2.start()
