import threading
var=1
class MinhaThread(threading.Thread):
	def run(self):
		global var
		print('Thread %d'%var)
		var+=1
for x in range(20):
	MinhaThread().start()