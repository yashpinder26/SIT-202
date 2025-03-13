import socket  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(('', 11500))  

while True:
    data, addr = s.recvfrom(1024)  
    message = data.decode()
    char_count = len(message)
    response = f"{char_count} {message.upper()}"
    
    print(f"Received message from {addr}: {message} ({char_count} characters)")  
    s.sendto(response.encode(), addr)  
