from socket import *

servername="127.0.0.1"
serverport=12332

server_socket = socket(AF_INET,SOCK_STREAM)

'''
Assegna la socket lato server alla porta definita nella variabile serverport
'''
server_socket.bind(('',serverport))

'''
mi metto in ascolto di richieste TCP da parte dei client. Il parametro è il numero massimo
di connessioni da tenere in coda.
Attende finchè qualche client non "bussi alla porta"
'''
server_socket.listen(1)

while True:
	'''
	blocca temporaneamente l'esecuzione del programma finchè il client
	non "bussa alla porta di benvenuto"
	Nel riprendere la connessione viene creata una socket dedicata allo specifico
	client. 
	Client e server completano a questo punto la procedura di Handshake
	'''
	connection_socket,addr = server_socket.accept()
	message,_ = connection_socket.recvfrom(1024)
	print(f"New conncetion recieved from {addr}. Payload: {message}")
	modified_message = message.lower()
	connection_socket.send(modified_message)
	'''
	chiudo la connessione con quello specifico client. 
	Nota che poichè server_socket rimane aperta, altri client potrannop "bussare alla porta "
	'''
	connection_socket.close()
