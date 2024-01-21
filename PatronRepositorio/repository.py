from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

Base = declarative_base()
Base.metadata.create_all(bind=engine)

class UserRepository:
    def __init__(self, session):
        self.session = session

    def add(self, user):
        self.session.add(user)
        self.session.commit()

    def get(self, id):
        return self.session.query(User).filter_by(id=id).first()

    def get_all(self):
        return self.session.query(User).all()

    def delete(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        self.session.delete(user)
        self.session.commit()

@app.route('/users', methods=['POST'])
def add_user():
    name = request.json['name']
    age = request.json['age']
    new_user = User(name, age)
    user_repository.add(new_user)
    return 'User added successfully', 200

@app.route('/users', methods=['GET'])
def get_all_users():
    users = user_repository.get_all()
    return '\n'.join([str(user) for user in users])

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = user_repository.get(id)
    if user:
        return str(user)
    else:
        return 'User not found', 404

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user_repository.delete(id)
    return 'User deleted successfully', 200

if __name__ == '__main__':
    user_repository = UserRepository(db.session)
    app.run(debug=True)