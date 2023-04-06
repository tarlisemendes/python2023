#pip install Flask-SQLAlchemy
#comando terminal pra instalar sqlalchemy
# pip install mysqlclient
#instalar o banco SQl muy sqlclient

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'chave_secreta'

#usando o prompt do mySQL command line, vamos criar uma base de dados
#create data base bancodados

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:softgraf@localhost:3306/bancodados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lc4_0YlAAAAANA_NwoNa41IZCNxYPrGyXOhherZ'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lc4_0YlAAAAABaw1eXfqu6wcpffUU3EOx7BziYc'
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_OPTIONS'] = {'theme' : 'white'}


db = SQLAlchemy(app)
lista = []


