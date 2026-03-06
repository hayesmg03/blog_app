from flask import Flask, render_template
import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy

password = os.environ['DB_PASS']

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://postgres:{password}@localhost/5432'

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'
    user_name=db.Column(db.String(40),primary_key=True)
    email=db.Column(db.String(40))

    def __init__(self, email):
        self.email=email

@app.route("/")
def index():
    return render_template('index.html')

