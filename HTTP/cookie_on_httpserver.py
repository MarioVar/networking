from socket import *
import random
from datetime import datetime

users = {}

servername = "127.0.0.1"
serverport = 80

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', serverport))
server_socket.listen(1)

def get_cookie_value(request, cookie_name):
    # Split the request into lines
    lines = request.split('\r\n')
    # Look for the Cookie header
    for line in lines:
        if line.startswith('Cookie:'):
            # Split the Cookie header into individual cookies
            cookies = line.split(': ')[1].split(';')
            # Iterate over the cookies to find the one with the specified name
            for cookie in cookies:
                name, value = cookie.split('=')
                if name.strip() == cookie_name:
                    return value.strip()
    # Cookie not found
    return None

def handle_http_request(request, src_addr):
    # Estrai il percorso dalla richiesta HTTP GET
    set_cookie=False
    try:
        path = request.split(' ')[1]
        user_id = get_cookie_value(request, 'user_id')
        if user_id == None:
            set_cookie=True

            random_number = random.randint(5, 9999)
            user_id = f"{src_addr}-{random_number}"
            users[user_id]=f"[{datetime.now().isoformat()}] user visited page {path}. "
        else:
            users[user_id] += f"[{datetime.now().isoformat()}] user visited page {path}. "
        print(f"Activities of the user {user_id}: {users[user_id]}")
        # Se il percorso è la radice, restituisci una pagina di benvenuto e imposta un cookie
        if path == '/':
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            if set_cookie:
                response += f"Set-Cookie: user_id={user_id}\r\n"
            response += "\r\n"
            response += "<html><body><h1>Benvenuto!</h1>"
            response += "<p>Questo &egrave il tuo primo accesso.</p>"
            response += "</body></html>"
        # Se il percorso è '/anche', restituisci una pagina e aggiorna il cookie
        elif path == '/anche':
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            if set_cookie:
                response += f"Set-Cookie: user_id={user_id}\r\n"
            response += "\r\n"
            response += "<html><body><h1>Pagina Anche</h1>"
            response += "<p>Benvenuto di nuovo! Hai visitato anche questa pagina.</p>"
            response += "</body></html>"
        # Se il percorso è '/test', restituisci una pagina e aggiorna il cookie
        elif path == '/test':
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            if set_cookie:
                response += f"Set-Cookie: user_id={user_id}\r\n"
            response += "\r\n"
            response += "<html><body><h1>Pagina Test</h1>"
            response += "<p>Benvenuto di nuovo! Hai visitato anche questa pagina.</p>"
            response += "</body></html>"
        # Se il percorso è '/recap', restituisci una lista di tutti gli utenti e le loro attività
        elif path == '/recap':
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            response += "<html><body><h1>Recap Utenti</h1>"
            response += "<ul>"
            for user, activity in users.items():
                response += f"<li><strong>User:</strong> {user}, <strong>Activity:</strong> {activity}</li>"
            response += "</ul>"
            response += "</body></html>"
        # Se il percorso non corrisponde a nessuna delle pagine gestite, restituisci un errore 404
        else:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            response += "<html><body><h1>Errore 404 - Pagina non trovata</h1></body></html>"
    except IndexError:
        # Se non riesci a estrarre il percorso, restituisci un errore 400
        response = "HTTP/1.1 400 Bad Request\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += "<html><body><h1>Errore 400 - Richiesta non valida</h1></body></html>"
    return response

def start_server():
    while True:
        connection_socket, addr = server_socket.accept()
        request, _ = connection_socket.recvfrom(1024)
        # Converte i byte della richiesta in una stringa
        request_str = request.decode('utf-8')
        print(f"New connection received from {addr}. Payload: {request_str}")
        # Elabora la richiesta HTTP e ottieni la risposta
        response = handle_http_request(request_str, addr)
        # Invia la risposta al client
        connection_socket.send(response.encode('utf-8'))
        # Chiudi la connessione con il client
        connection_socket.close()

if __name__ == "__main__":
    start_server()

