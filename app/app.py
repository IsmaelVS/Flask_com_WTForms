# coding: utf-8
"""Formulário web utilizando Flask e WTForms."""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from wtforms import Form, PasswordField, StringField, SubmitField

app = Flask(__name__)

db = SQLAlchemy(app)

lm = LoginManager(app)


class Usuario(db.Model):
    """Classe para criação da tabela usuário no banco."""

    __tablename__ = 'usuario'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        db.create_all()
        self.username = username
        self.password = password


class Login(Form):
    """Classe para montar o formulário."""

    login = StringField('Username')
    password = PasswordField('Password')
    btn = SubmitField('Logar')


class Cadastro(Form):
    """Classe para montar o formulário de cadastro."""

    login = StringField('Username')
    password = PasswordField('Password')
    btn = SubmitField('Cadastrar')


@app.route('/login')
def login():
    """Rota inicial, exibe o template do formulário."""
    return render_template('login.html', form=Login())


@app.route('/check_login', methods=['POST'])
def check_login():
    """Rota para validar dados do formulário."""
    if validate_login(request.form['login'], request.form['password']):
        return 'Logado com sucesso!!'
    return render_template('login.html', form=Login(), error=True)


def validate_login(user, senha):
    """Função de validação dos dados do formulário."""
    return db.session.query(Usuario).filter_by(username=user).first()


@app.route('/')
def home():
    """Rota inicial, com formulário para cadastro."""
    return render_template('cadastro.html', form=Cadastro())


@app.route('/checar_cadastro', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    username = request.form['login']
    password = request.form['password']
    user = Usuario(username, password)
    db.session.add(user)
    db.session.commit()
    return render_template('login.html', form=Login())
