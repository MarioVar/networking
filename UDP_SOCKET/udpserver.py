from socket import *

servername="127.0.0.1"
serverport=12345

server_socket = socket(AF_INET,SOCK_DGRAM)

'''
Assegna la socket lato server alla porta definita nella variabile serverport
'''
server_socket.bind(('',serverport))


#mi metto in ascolto di richieste
while True:
	message,client_address = server_socket.recvfrom(2048)
	print(f"New conncetion recieved from {client_address}. Payload: {message}")
	modified_message = message.lower()
	server_socket.sendto(modified_message,client_address)
