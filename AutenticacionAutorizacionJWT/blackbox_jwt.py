from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, jwt_refresh_token_required, create_refresh_token
import datetime

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret' # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=30)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=30)

jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'test' or password != 'test':
        return jsonify({'login': False}), 401

    # Define the user identity
    user_identity = {'username': username}

    # Create the access and refresh tokens
    access_token = create_access_token(identity=user_identity)
    refresh_token = create_refresh_token(identity=user_identity)

    return jsonify(access_token=access_token, refresh_token=refresh_token)


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    # Create a new access token
    user_identity = get_jwt_identity()
    access_token = create_access_token(identity=user_identity)

    return jsonify(access_token=access_token)


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username)


if __name__ == '__main__':
    app.run(port=5000)