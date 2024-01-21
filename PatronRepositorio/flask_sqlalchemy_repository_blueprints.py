# Importando librerías
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Creando instancia de la aplicación Flask
app = Flask(__name__)

# Configurando la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/basededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando el objeto SQLAlchemy
db = SQLAlchemy(app)

# Definición del modelo de datos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Creación del repositorio de productos
class ProductoRepository:
    def __init__(self):
        self.session = db.session

    def add(self, producto):
        self.session.add(producto)
        self.session.commit()

    def delete(self, id):
        producto = self.get(id)
        if producto:
            self.session.delete(producto)
            self.session.commit()

    def get(self, id):
        return self.session.query(Producto).get(id)

    def get_all(self):
        return self.session.query(Producto).all()

    def update(self, id, data):
        producto = self.get(id)
        if producto:
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            self.session.commit()

# Creación del blueprint para el controlador de productos
from flask import Blueprint

productos_blueprint = Blueprint('productos', __name__)

repo = ProductoRepository()

@productos_blueprint.route('/productos', methods=['GET'])
def get_productos():
    productos = repo.get_all()
    return jsonify([producto.as_dict() for producto in productos])

@productos_blueprint.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = repo.get(id)
    if producto:
        return jsonify(producto.as_dict())
    else:
        return jsonify({"message": "Producto no encontrado"}), 404

@productos_blueprint.route('/productos', methods=['POST'])
def add_producto():
    data = request.get_json()
    producto = Producto(data['nombre'], data['precio'])
    repo.add(producto)
    return jsonify(producto.as_dict()), 201

@productos_blueprint.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    data = request.get_json()
    repo.update(id, data)
    return jsonify({"message": "Producto actualizado satisfactoriamente"}), 200

@productos_blueprint.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    repo.delete(id)
    return jsonify({"message": "Producto eliminado satisfactoriamente"}), 200

# Registrando el blueprint en la aplicación Flask
app.register_blueprint(productos_blueprint)

# Inicializando la base de datos
db.create_all()

# Iniciando la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)