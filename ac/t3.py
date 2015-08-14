from threading import Thread
def printnome(nome):
	#while True:
	print(nome)
	
th=Thread(target=printnome,args="a2")
th.start()


#Thread(target=printnome).start()
