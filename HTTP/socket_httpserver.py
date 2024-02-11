from socket import *

servername = "127.0.0.1"
serverport = 80

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', serverport))
server_socket.listen(1)

def handle_http_request(request):
    # Estrai il percorso dalla richiesta HTTP GET
    try:
    	#EX: GET /test HTTP/1.1 -> path = /test
        path = request.split(' ')[1]
        # Se il percorso è la radice, restituisci una pagina di benvenuto
        if path == '/':
            return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Benvenuto!</h1></body></html>"
        # Se il percorso è diverso, restituisci una pagina di errore 404
        else:
            return "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Errore 404 - Pagina non trovata</h1></body></html>"
    except IndexError:
        # Se non riesci a estrarre il percorso, restituisci una pagina di errore 400
        return "HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Errore 400 - Richiesta non valida</h1></body></html>"

while True:
    connection_socket, addr = server_socket.accept()
    request, _ = connection_socket.recvfrom(1024)
    
    # Converte i byte della richiesta in una stringa
    request_str = request.decode('utf-8')
    
    print(f"New connection received from {addr}. Payload: {request_str}")
    
    # Elabora la richiesta HTTP e ottieni la risposta
    response = handle_http_request(request_str)
    
    # Invia la risposta al client
    connection_socket.send(response.encode('utf-8'))
    
    # Chiudi la connessione con il client
    connection_socket.close()

