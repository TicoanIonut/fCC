import socket

HOST = '192.168.1.133'
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
	communication_socket, adress = server.accept()
	print(f'Connected to {adress}')
	message = communication_socket.recv(1024).decode('utf-8')
	print(f'Message from client is {message}')
	communication_socket.send(f'Got your message! Danke'.encode('utf-8'))
	communication_socket.close()
	print(f'Connection with {adress} ended!')
	