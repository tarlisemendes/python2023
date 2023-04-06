#principal.py

from flask import Flask, render_template, request, redirect, url_for, session, flash

from produto import Produto

from dao import ProdutoDao

#para instalas o flask por comando:
#1 . acessar o terminal
#2 . acessar venv: Cd venv
#3 .  acessar scripts: CD scripts
#4 . para vizualizar arquivos: DIR
#5 . .\pip install flask
#ou para instalar uma versão especifica. EX:
# .\pip install flask=2.0.2


#lista



produto_dao = ProdutoDao('bancodados.db')

#criar um app do flask
app = Flask(__name__)
app.secret_key = 'softgraf'


@app.route('/')
def index():
    lista = produto_dao.listar()
    return render_template('relatorio.html', titulo='Relatorio estoque', produtos=lista)


@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        return render_template('cadastrar.html', titulo='Cadastra Novo Produto')

@app.route('/editar/<string:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        produto = produto_dao.busca_por_id(id)
        return render_template('editar.html', titulo='Editar Produto', produto=produto)

@app.route('/salvar', methods= ['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    produto =Produto(descricao, preco, quantidade, id)
    produto_dao.salvar(produto)
    return redirect(url_for('index'))

@app.route('/deletar/<string:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        produto_dao.deletar(id)
        flash('o produto foi removido com sucesso!')
        return redirect(url_for('index'))

@app.route('/login')
def login():
    #verifica se o usuario esta logado
    if 'usuario_logado' in session and session['usuario_logado'] !=None:
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']

    #se login OK cria uma sessao
    if usuario == 'tarlise' and senha == '123':
        session['usuario_logado'] = usuario
        flash(usuario +' logou com sucesso!')
        return redirect(url_for('index'))
    else:
        flash('Senha invalida! tente novamente.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('nenhum usuario logado')
    return (redirect(url_for('index')))




if __name__=='__main__':
    app.run(debug=True)
