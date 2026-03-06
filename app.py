from flask import Flask, render_template
import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy

password = os.environ['DB_PASS']

app = Flask(__name__)

conn = psycopg2.connect(database="postgres",
                        user='postgres',
                        password=f'{password}',
                        host='localhost', port='5432')
cur = conn.cursor()

cur.execute(
    
)

conn.commit()

@app.route("/")
def index():
    return render_template('index.html')



cur.close()
conn.close()