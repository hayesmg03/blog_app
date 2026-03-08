from flask import Flask, render_template
import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy

password = os.getenv("DB_PASS")

app = Flask(__name__)


@app.route("/")
def index():
    conn = psycopg2.connect(database="postgres",
                        user='postgres',
                        password=f'{password}',
                        host='localhost', port='5432')
    cur = conn.cursor()

    name = cur.execute(
        "SELECT UserName FROM users WHERE Email is 'email@email.com'"
    )

    cur.close()
    conn.close() 

    return render_template('index.html', name=name)

