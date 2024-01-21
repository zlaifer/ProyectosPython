
from functools import wraps
from flask import Flask, request, jsonify
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)

# Configuration for encryption and decryption
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['ALGORITHM'] = 'HS256'

# Serializer
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

def authenticate_middleware(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        try:
            auth_token = auth_header.split(' ')[1]
            data = serializer.loads(auth_token, max_age=60)
        except:
            return jsonify({'error': 'Invalid token or token expired'}), 401

        return f(*args, **kwargs)
    return wrapper

@app.route('/encode', methods=['POST'])
def encode():
    payload = request.get_json()
    token = serializer.dumps(payload)
    return jsonify({'token': token})

@app.route('/decode', methods=['POST'])
@authenticate_middleware
def decode():
    auth_header = request.headers.get('Authorization')
    auth_token = auth_header.split(' ')[1]
    data = serializer.loads(auth_token)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)