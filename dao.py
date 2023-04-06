#dao = data access Objectc ou objetio de acessos a dados
#modulo responsavel pelo acesso ao banco de daos
import sqlite3

from produto import Produto

SQL_PREPARA_BANCO = 'create table if not exists produto(' \
                        'descricao varchar(60) not null,' \
                        'preco double not null,' \
                        'quantidade integer not null' \
                    ');'


SQL_SALVA_PRODUTO = 'insert into produto values(?,?,?)'
SQL_LISTA_PRODUTOS= 'SELECT descricao, preco, quantidade,rowid FROM produto'
SQL_PRODUTO_POR_ID = 'SELECT descricao, preco, quantidade,rowid FROM produto WHERE rowid=?'
SQL_ATUALIZA_PRODUTO = 'UPDATE produto SET descricao=?, preco=?, quantidade=? WHERE rowid=?'
SQL_DELETA_PRODUTO = 'DELETE FROM produto WHERE rowid=?'



class ProdutoDao:

    def __init__(self, nome_banco):
        self.__nome_banco = nome_banco
        self.prepara_banco()


    def prepara_banco(self):
        print('conctando com o banco de dados...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_PREPARA_BANCO)
        #comitando senao nada tera efeito
        conexao.commit()
        print('OK')

    def salvar(self, produto):
        #print('Testando ID:', produto.id)
        #print('Salvando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        #verifica se existe um id valido
        if (produto.id != None and len(produto.id) > 0):
            cursor.execute(SQL_ATUALIZA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade, produto.id))
        else:
            cursor.execute(SQL_SALVA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade))
            produto.id = cursor.lastrowid
        conexao.commit()
        print('OK')
        return produto #devolve mesmo produto, porem agora com o Id

    def listar(self):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_LISTA_PRODUTOS)
        #Converte a lista de dados em lista de objetos tipo produto
        produtos = traduz_produtos(cursor.fetchall())
        return produtos

    def deletar(self, id):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_DELETA_PRODUTO, [str(id)])
        conexao.commit()

    def busca_por_id(self, id):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_PRODUTO_POR_ID, [str(id)])
        tupla = cursor.fetchone()
        return cria_produto_com_tupla(tupla)

#lista_tuplas =[('TV LG 50', 3999.0, 5, 2), ('computador', 5200.0, 5, 4), ('computador', 3200.0, 5, 5),
# ('guarda -roupa', 1800.0, 3, 6), ('1111', 111.0, 222, 7), ('45454', 4545.0, 555, 8), ('tv', 123.0, 5, 9), ('sofa', '123,00', 5, 10)]

def traduz_produtos(lista_tuplas):
    return list(map(cria_produto_com_tupla, lista_tuplas))

 #   [('TV LG 50', 3999.0, 5, 2),

def cria_produto_com_tupla(tupla):
    return Produto(tupla[0], tupla[1],tupla[2], tupla[3])