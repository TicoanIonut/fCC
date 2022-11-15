import socket

HOST = '192.168.1.133'
PORT = 9090

socket = socket.socket(socket.AF_IRDA, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
socket.send("Hello World".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
