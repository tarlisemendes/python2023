#Projeto baseado em ORM(object relacional - mapping = mapeamento Objeto-relacional)
#Framework: FLASK-SQLALCHEMY
#converte objetos em tabelas relacionais(SQL)

#Site oficial:
#https://flask-sqlalchemy.palletsprojects.com

#No terminal do pycharm
#pip install Flask flask-SQLAlchemy

#Caso ocorra erro de segurança, mudar a politica de segurança do power shell
# a. Executar powershell como administrador
# b. PS C:\Windows\system32> Get-executionPolicy
# Restricted
#
# c. PS C:\Windows\system32> Set-executionPolicy Remotesigned
# d. PS C:\Windows\system32> Get-executionPolicy
# RemoteSigned

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Configurando acesso ao banco de dados MySQL:
#mysql://username:password@host:port/database_name
#mysql://root:softgraf@localhost:3306/nome_banco

# Configurando acesso ao banco de dados PostgreSQL:
#postgresql://username:password@host:port/database_name

#Configurando para sqlite
#D:\Curso python tarlise\projeto_alchemy
basedir = os.path.abspath(os.path.dirname(__file__))

# 'sqlite:///E:\cursoPython Tarlise\pythonProject\pythonProject\projeto_alchemy\database.db'
uri = 'sqlite:///' + os.path.join(basedir, 'database.db')

#cria a aplicacao flask
app = Flask(__name__)
#configura o SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_ModiFiCATIONS'] = False

#Criar um objeto para o acesso ao banco de dados
db = SQLAlchemy(app)






