from flask import render_template, redirect, request, session, flash

from config import app, db, lista
from formularios import FormCadastro
from models import Login

@app.route('/')
def home():
    if not session:
        session['login'] = None
    #cria todas as tabelas(login) no banco de dados
    db.create_all()
    #carrega todos os dados de login
    lista = Login.query.all()
    return render_template('inicial.html', lista=lista)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if session ['login'] == None:
        flash('nenhum usuario logado')
        return redirect('/')

    form = FormCadastro()
    return render_template('formulario.html', form=form)

@app.route('/salvar',methods=['GET','POST'])
def salvar():
    form = FormCadastro()
    if form.validate_on_submit():
        nome = form.nome.data
        idade = form.idade.data
        email = form.email.data
        senha = form.senha.data
        if Login.query.filter_by(email=email).first():
            form.email.errors.clear()
            form.email.errors.append('Este email ja esta cadastrados, use outro!!!')
            return render_template('formulario.html', form=form)
        else:
            #salva cadastro no banco
            cadastro = Login(nome, idade, email,senha)
            db.session.add(cadastro)
            db.session.commit()
            lista.append(cadastro)
            return render_template('inicial.html', lista=lista)

    else:
        form.recaptcha.errors.clear()
        form.recaptcha.errors.append('voce precisa validar o CAPTCHA')
        return render_template('formulario.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    login = Login.query.filter_by(email=email).first()
    if login and login.verificarSenha(senha):
        session['login'] = login.nome
        flash(login.nome + 'esta logado(a)')
        return redirect('/')
    else:
        flash('E-mail e/ou senha invalido!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['login'] = None
    flash('Nenhum usuario logado')
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
