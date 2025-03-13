import socket
ob=socket.socket()
ob.connect(
    ("127.0.0.1",11500)
)
print(ob.recv(1024).decode())
ob.send(input("Enter the msg: ").encode())