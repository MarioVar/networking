from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Stampa tutti i campi della richiesta ricevuta
    print("Request Method:", request.method)
    print("Request URL:", request.url)
    print("Request Headers:", request.headers)
    print("Request Data:", request.data)
    print("Request Form:", request.form)
    print("Request Args:", request.args)
    print("Request Cookies:", request.cookies)
    
    # Altri dettagli disponibili sulla richiesta
    print("Request Remote Address:", request.remote_addr)
    print("Request User Agent:", request.user_agent)
    print("Request Content Type:", request.content_type)
    print("Request Content Length:", request.content_length)

    # Esegui la logica della tua applicazione
    response = 'Hello, World!'

    # Stampa tutti i campi della risposta inviata
    print("Response:", response)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)

