from twilio.rest import Client 
 
def enviarMensagem(telefone,mensagem):
    account_sid = 'xxxx' 
    auth_token = 'xxxx' 
    client = Client(account_sid, auth_token) 
    body=("'{}'".format(mensagem))
    print(body)
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='{}'.format(mensagem),      
                                to='{}'.format(telefone) 
                            ) 
    
    print(message.sid)