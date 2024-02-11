from socket import *

'''
puo contenere l'hostname del server o l'ip nel caso di hostname viene fatta
una ricerca dns per ottenere l'ip e successivamente partirà la richiesta UDP
'''
servername="127.0.0.1"
serverport=12345

'''
creazione di una socker lato client
	- AF_INET: stiamo dicendo che la rete sottostante è ipv4
	- DOCK_DGRAM: specifichiamo che è una socket UDP piuttosto che TCP
Essendo una socket lato client non serve che specifichiamo il numero di porta, esso sarà scelto tra quelli disponibili
'''
client_socket = socket(AF_INET,SOCK_DGRAM)

message = b"HELLO WORLD!"
'''
In questa parte di codice viene agganciato l'indirizzo di destinazione al messaggio e spedito
nota che al pacchetto è attaccato anche l'indirizzo sorgente ma questa operazione a noi è trasparente è fatta in automatico
'''
client_socket.sendto(message,(servername,serverport))

'''
ci aspettiamo una risposta dal server
'''
modified_message, server_address = client_socket.recvfrom(2048)

print(f"The message recieved from the server {server_address}: {modified_message}")

client_socket.close()
