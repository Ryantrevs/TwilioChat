from flask import Flask,request
import requests
from DefineRequest import DefineResponse
from twilio.rest import Client 

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def funciona():
    telefone = request.values.get('From','').lower()
    mensagem = request.values.get('Body','').lower()
    print("Mensagem Recebida"+mensagem)
    DefineResponse.Definir(telefone,mensagem)
    return 'ok'

if __name__ == '__main__':
   app.run(debug=True)