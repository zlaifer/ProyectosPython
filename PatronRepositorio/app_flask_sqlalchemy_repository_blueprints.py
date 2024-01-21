from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'
db = SQLAlchemy(app)

# Definición del modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

# Definición del repositorio
class UserRepository:
    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def create_user(self, name):
        user = User(name)
        db.session.add(user)
        db.session.commit()
        return user

# Definición de los blueprints
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    user_repository = UserRepository()
    users = user_repository.get_all_users()
    return 'Hello, {}!'.format(users[0].name)

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()
