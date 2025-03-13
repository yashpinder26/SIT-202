import socket			 
s = socket.socket()		 
print("Socket successfully created")

port = 11500			

s.bind(('', port))		 
print("Socket binded to %s" % (port)) 

s.listen(5)	 
print("Socket is listening")		 

while True: 
    c, addr = s.accept()	 
    print('Got connection from', addr)
 
    c.send('Thank you for connecting'.encode()) 

    message = c.recv(1024).decode()
    print("Message from client:", message)

    c.close()