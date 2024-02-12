const http = require('http');
const url = require('url');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  // Stampa tutti i campi della richiesta ricevuta
  console.log('Request Method:', req.method);
  console.log('Request URL:', req.url);
  console.log('Request Headers:', req.headers);
  console.log('Request Body:', req.body); // Dipende dal tipo di richiesta (GET, POST, ecc.)
    // Stampare eventuali cookies
  console.log('Request Cookies:', req.headers.cookie);

  // Stampare l'indirizzo remoto
  console.log('Request Remote Address:', req.socket.remoteAddress);

  // Stampare il tipo di contenuto
  console.log('Request Content Type:', req.headers['content-type']);

  // Stampare l'agente utente
  console.log('Request User Agent:', req.headers['user-agent']);

  // Stampare la lunghezza del contenuto
  console.log('Request Content Length:', req.headers['content-length']);
    
  // Parsing dell'URL per ottenere l'URI e i parametri della query
  const parsedUrl = url.parse(req.url, true);
  console.log('Request URI:', parsedUrl.pathname);
  console.log('Request Query Params:', parsedUrl.query);
  
  
  // Esegui la logica della tua applicazione
  const response = 'Hello, World!';

  // Stampa tutti i campi della risposta inviata
  console.log('Response:', response);

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end(response);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

