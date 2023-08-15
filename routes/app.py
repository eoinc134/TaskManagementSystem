from flask import Flask, render_template, session

from ..model.sql.Sql import Sql

app = Flask(__name__)

@app.route('/')
def home_page():
    conn = get_db_connection()
    cursor = conn.cursor()

    lists = cursor.execute("SELECT * FROM Lists").fetchall()

    return render_template('home_page.html', lists=lists)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/validateRegistration')
def validateRegistration():
    return render_template('home_page.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validateLogin')
def validateLogin():
    session['login'] = True
    return render_template('home_page.html', data=session['login'])

@app.route('/logout')
def logout():
    session.clear()
    return render_template('home_page.html')

def get_db_connection():
    database = Sql()
    return database.cnxn
