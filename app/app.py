from flask import Flask, render_template, request
from wtforms import Form, PasswordField, StringField, SubmitField

app = Flask(__name__)


class Login(Form):
    login = StringField()
    password = PasswordField()
    btn = SubmitField('Logar', )


@app.route('/')
def home():
    return render_template('login.html', form=Login())


@app.route('/check_login', methods=['POST'])
def check_login():
    if validate_login(request.form['login'], request.form['password']):
        return 'Logado com sucesso!!'
    return 'Usuário ou senha inválido'


def validate_login(user, senha):
    return user == 'teste' and senha == '123'
