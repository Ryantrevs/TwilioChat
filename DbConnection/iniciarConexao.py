import mysql.connector 
from mysql.connector import errorcode

def iniciar():
	try:
		dbConnection = mysql.connector.connect(host='localhost',user='root',password='xxxx',database='chatbotdb')
		return dbConnection
	except mysql.connector.Error as error:
		if error.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database doesn't exist")
		elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("User name or password is wrong")
		else:
			print(error)
	else:
		dbConnection.close()
	return

def selectTelefone(telefone,db):
	cursor = db.cursor()
	sql = ("SELECT * FROM cliente where numero='{}'".format(telefone))
	cursor.execute(sql)
	resultado = cursor.fetchone()
	cursor.close()
	return resultado

def InsertTelefone(telefone,db):
	cursor = db.cursor()
	sql = ("INSERT INTO chatbotdb.cliente (numero) VALUES ('{}')".format(telefone))
	cursor.execute(sql)
	db.commit()
	result = cursor.rowcount
	cursor.close()
	return result

def InsertInfo(telefone,mensagem,db,campo):
	cursor = db.cursor()
	sql = ("UPDATE chatbotdb.cliente SET {} = '{}' where numero='{}'".format(campo,mensagem,telefone))
	print (sql)
	cursor.execute(sql)
	db.commit()
	result = cursor.rowcount
	cursor.close()
	return result

