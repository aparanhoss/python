import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.0.201', 4998))
clientsocket.send('sendir,2:3,1,38699,1,1,170,168,22,62,22,20,22,62,22,62,22,20,22,20,22,62,22,20,21,21,22,62,22,20,22,20,22,62,22,62,22,20,22,62,21,21,22,62,22,62,22,62,22,62,22,20,22,62,22,62,21,63,22,20,22,20,22,20,22,20,22,62,22,20,22,20,21,63,22,62,22,62,22,20,22,20,22,20,22,20,22,20,21,21,22,20,22,20,22,62,22,62,22,62,22,62,22,62,21,201,169,168,22,62,22,20,22,62,22,62,22,20,22,20,22,62,22,20,21,21,22,62,22,20,22,20,22,62,22,62,22,20,22,62,21,21,22,62,22,62,22,62,22,62,22,20,22,62,22,62,21,63,22,20,22,20,22,20,22,20,22,62,22,20,22,20,21,63,22,62,22,62,22,20,22,20,22,20,22,20,22,20,21,21,22,20,22,20,22,62,22,62,22,62,22,62,22,62,21,4953\r\n\r\n')
clientsocket.send('sendir,2:3,1,38699,1,1,170,168,22,62,22,20,22,62,22,62,22,20,22,20,22,62,22,20,21,21,22,62,22,20,22,20,22,62,22,62,22,20,22,62,21,21,22,62,22,62,22,62,22,62,22,20,22,62,22,62,21,63,22,20,22,20,22,20,22,20,22,62,22,20,22,20,21,63,22,62,22,62,22,20,22,20,22,20,22,20,22,20,21,21,22,20,22,20,22,62,22,62,22,62,22,62,22,62,21,201,169,168,22,62,22,20,22,62,22,62,22,20,22,20,22,62,22,20,21,21,22,62,22,20,22,20,22,62,22,62,22,20,22,62,21,21,22,62,22,62,22,62,22,62,22,20,22,62,22,62,21,63,22,20,22,20,22,20,22,20,22,62,22,20,22,20,21,63,22,62,22,62,22,20,22,20,22,20,22,20,22,20,21,21,22,20,22,20,22,62,22,62,22,62,22,62,22,62,21,4953\r\n\r\n')