from models import Produto
from config import db, app

with app.app_context():
    #deleta todos os dados do banco
    db.drop_all()
    db.create_all()

    #Cria uma entidade: é um objeto que representa um registro no banco de dados
    #esse objeto est guardado somente na memoria,por enquanto
    tv = Produto(descricao='tv Sansung', preco=1999.99, quantidade =10)


    #mostra os dados do objeto Tv
    print(tv.id)
    print(tv.descricao)

    #salva no banco usando SQLAlchemy ORM
    db.session.add(tv)   #INSERT
    db.session.commit()

    #agr tem id
    print(tv.id)

    #alterando - >>  #UPDATE#
    tv.descricao = 'TV LG 50'
    db.session.add(tv)
    db.session.commit()

    #Criando outra entidade
    fogao = Produto(descricao ='Fogao a gás 4 bocas', preco=599.90, quantidade=10)

    #salva no banco
    db.session.add(fogao)
    db.session.commit()

    #lista todas as entidade
    #SELECT * from Produto;
    produtos = Produto.query.all()
    print(produtos)

    #buscando um unico registro
    porId = Produto.query.filter_by(id=1).first()
    print(porId)

    #buscando por descricao
    porDescricao = Produto.query.filter_by(descricao='Fogao a gás 4 bocas').all()
    print(porDescricao)

    #apagar um registro
    produto = Produto.query.filter_by(id=2).first()
    if produto:
        db.session.delete(produto)
        db.session.commit()
        print('apagou')
    else:
        print('nao apagou')