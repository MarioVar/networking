from socket import *

'''
puo contenere l'hostname del server o l'ip nel caso di hostname viene fatta
una ricerca dns per ottenere l'ip e successivamente partirà la richiesta UDP
'''
servername="127.0.0.1"
serverport=12332

'''
creazione di una socker lato client
	- AF_INET: stiamo dicendo che la rete sottostante è ipv4
	- SOCK_STREAM: specifichiamo che è una socket UDP piuttosto che TCP
Essendo una socket lato client non serve che specifichiamo il numero di porta, esso sarà scelto tra quelli disponibili
'''
client_socket = socket(AF_INET,SOCK_STREAM)

message = b"HELLO WORLD!"

'''
In TCP prima di inviare i dati devo stabilire un canale ovvero iniziare un Handshake e stabilire una connessione con il server
'''
client_socket.connect((servername,serverport))

'''
non uso sendto come in udp, perchè gho stabilito già un canale TCP di connessione
Mentre prima in udp attaccavamo al pacchetto la destinazione. QUi in TCP abbiamo instaurato già un canale quindi ora dobbiamo solo lasciar cadere i byte da inviare 
'''
client_socket.send(message)

'''
ci aspettiamo una risposta dal server
'''
modified_message, server_address = client_socket.recvfrom(1024)

print(f"The message recieved from the server {server_address}: {modified_message}")

client_socket.close()
