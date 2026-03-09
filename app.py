from flask import Flask, render_template
import os
from dotenv import load_dotenv
import psycopg2
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    conn = psycopg2.connect(database="postgres",
                        user='postgres',
                        password=f'{os.getenv("DB_PASS")}',
                        host='localhost', port='5432')
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM posts WHERE PostId = 1"
    )
    query_results = cur.fetchone()

    user_name = query_results[2]
    title = query_results[3]
    desc = query_results[4]

    cur.close()
    conn.close() 

    return render_template('index.html', user_name=user_name, title=title, desc=desc)

