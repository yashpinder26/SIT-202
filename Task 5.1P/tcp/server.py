import socket

HOST = '127.0.0.1' 
PORT = 65432        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    if not data:
        break
    
    print(f"Received message: {data}")
    
    char_count = len(data)
    uppercase_msg = data.upper()
    
    response = f"{char_count} {uppercase_msg}"
    conn.send(response.encode())

    conn.close()

