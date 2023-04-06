from sqlalchemy.sql import func
from config import db


#ORM - converte uma classe em uma tabela relacional
#Representa uma entidade do banco de dados

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer)
    cadastrado = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Produto: {self.id} desc{self.descricao} preco:{self.preco} quant:{self.quantidade} ' \
               f'data:{self.cadastrado}>'