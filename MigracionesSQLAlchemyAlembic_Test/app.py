# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PgBlackList202314@localhost:5432/pgblacklistdb'
db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(13), default="ACT")
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow)
    email = db.Column(db.String(64), unique=True)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

