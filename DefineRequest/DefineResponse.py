from DbConnection import iniciarConexao
import mysql.connector 
from Response import response
from Entity import Cliente

def Definir(telefone,mensagem):
    db = iniciarConexao.iniciar()
    dadosCliente = iniciarConexao.selectTelefone(telefone,db)
    print(dadosCliente)
    if(dadosCliente!=None):
        info = Cliente.DadosCliente(dadosCliente[0],dadosCliente[1],dadosCliente[2],dadosCliente[3])
        if(info.nome!=None):
            if(info.email!=None):
                if(info.curso!=None):
                    print(Funcinou)
                  
                else: 
                    iniciarConexao.InsertInfo(telefone,mensagem,db,"curso")
                    enviarMensagem = "Digite Agora o titulos do seu trabalho"
                    response.enviarMensagem(telefone,enviarMensagem)
            else:
                enviarMensagem = "Gostariamos de saber seu curso,\n\n digite por favor"
                iniciarConexao.InsertInfo(telefone,mensagem,db,"email")
                response.enviarMensagem(telefone,enviarMensagem)
                
        else:
            enviarMensagem = "Gostariamos de saber seu email,\n\n digite por favor"
            iniciarConexao.InsertInfo(telefone,mensagem,db,"nome")
            response.enviarMensagem(telefone,enviarMensagem)
    else:
        enviarMensagem = "Bem vindo ao Chat do Atenas Consultoria\n\n\nGostariamos de agradecer pela oportunidade\n\n Digite seu nome, por favor"
        iniciarConexao.InsertTelefone(telefone,db)
        response.enviarMensagem(telefone,enviarMensagem)


    