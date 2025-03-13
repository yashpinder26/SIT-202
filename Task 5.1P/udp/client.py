import socket  

ob = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server_address = ("127.0.0.1", 11500)  

message = "Hello"  
ob.sendto(message.encode(), server_address)  

data, _ = ob.recvfrom(1024)  
print("Received from server:", data.decode())  

ob.close()  
