# coding: utf-8
u"""Formulário web utilizando Flask e WTForms."""

from flask import Flask, render_template, request

from wtforms import Form, PasswordField, StringField, SubmitField

app = Flask(__name__)


class Login(Form):
    u"""Classe para montar o formulário."""
    login = StringField()
    password = PasswordField()
    btn = SubmitField('Logar', )


@app.route('/')
def home():
    u"""Rota inicial, exibe o template do formulário."""
    return render_template('login.html', form=Login())


@app.route('/check_login', methods=['POST'])
def check_login():
    u"""Rota para validar dados do formulário."""
    if validate_login(request.form['login'], request.form['password']):
        return 'Logado com sucesso!!'
    return 'Usuário ou senha inválido'


def validate_login(user, senha):
    u"""Função de validação dos dados do formulário."""
    return user == 'teste' and senha == '123'
