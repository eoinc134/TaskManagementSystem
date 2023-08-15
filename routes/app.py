from flask import Flask, render_template
import pandas as pd

from ..model.sql.Sql import Sql

app = Flask(__name__)

@app.route('/')
def home_page():
    conn = get_db_connection()
    cursor = conn.cursor()

    lists = cursor.execute("SELECT * FROM Lists").fetchall()

    return render_template('home_page.html', lists=lists)


def get_db_connection():
    database = Sql()
    return database.cnxn
