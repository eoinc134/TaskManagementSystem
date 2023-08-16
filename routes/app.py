from flask import Flask, render_template, session, redirect, url_for, request

from ..model.sql.Sql import Sql
from ..model.authentication.Login import emailExists, verifyPassword
from ..model.authentication.Register import validateEmail, validatePasswordStrength, passwordsEqual

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def home_page():
    session.clear()
    if session.get('login') == True:
        conn = get_db_connection()
        cursor = conn.cursor()

        lists = cursor.execute("SELECT * FROM Lists").fetchall()

        return render_template('home_page.html', lists=lists)
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

@app.route('/validateRegistration', methods=['POST'])
def validateRegistration():
    if emailExists(request.form.to_dict().get('email')):
        return render_template('register.html', error='Email is already in use')
    if not validateEmail(request.form.to_dict().get('email')):
        return render_template('register.html', error='This is not a valid email')
    if not validatePasswordStrength(str(request.form.to_dict().get('psw'))):
        return render_template('register.html', error='Password is not strong enough')
    if not passwordsEqual(request.form.to_dict().get('psw'), request.form.to_dict().get('repeat-psw')):
        return render_template('register.html', error='Passwords are not equals')   

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    if not emailExists(request.form.to_dict().get('email')):
        return render_template('login.html', error='Email does not exist')
    if not verifyPassword(request.form.to_dict().get('password')):
        return render_template('login.html', error='Password is incorrect')

    session['login'] = True
    return render_template('home_page.html', data=session['login'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

def get_db_connection():
    database = Sql()
    return database.cnxn
