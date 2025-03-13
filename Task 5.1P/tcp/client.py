import socket

HOST = '127.0.0.1'  
PORT = 65432       


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Hello SIT202"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Server Response: {response}")

client_socket.close()