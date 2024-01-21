from flask import Flask, request, jsonify
from functools import wraps
import datetime
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = '304a391c-9a28-11ee-b9d1-0242ac120002'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=1)

# Función para verificar el JWT y los permisos del usuario
def verify_token_and_permissions(permission):
    token = request.headers.get('Authorization')
    if not token:
        return False

    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        # Aquí puedes implementar la lógica para verificar los permisos del usuario
        # Puedes consultar el token decodificado y verificar los permisos necesarios
        # En este ejemplo, se asume que el usuario tiene permiso si el parámetro 'permission' es 'admin'
        return decoded_token.get('permission') == permission
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

# Decorador para verificar el JWT y los permisos antes de acceder al recurso
def requires_token_and_permission(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not verify_token_and_permissions(permission):
                return jsonify({'message': 'Acceso no autorizado'}), 401
            return f(*args, **kwargs)
        return decorated_function
    return decorator



# Ruta para generar un JWT
@app.route('/generar_token', methods=['POST'])
def generar_token():
    payload = request.json
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

# Ruta protegida que valida y decodifica el JWT
@app.route('/recurso', methods=['GET'])
def obtener_recurso():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Acceso no autorizado'}), 401
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        username = decoded_token.get('username')
        permission = decoded_token.get('permission')
        return jsonify({'user_id': user_id, 'username': username, 'permission': permission})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expirado'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token inválido'}), 401

# Ruta protegida que requiere un JWT con permiso de administrador
@app.route('/protected', methods=['GET'])
@requires_token_and_permission('admin')
def obtener_protected():
    token = request.headers.get('Authorization')
    decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    return decoded_token

    

# Ruta pública
@app.route('/publico', methods=['GET'])
def get_publico():
    return jsonify({'message': 'Acceso permitido al recurso público'})

if __name__ == '__main__':
    app.run()
