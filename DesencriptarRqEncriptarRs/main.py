from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Clave para encriptar y desencriptar
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.before_request
def decrypt_request():
    encrypted_data = request.data
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    request.data = decrypted_data

@app.after_request
def encrypt_response(response):
    encrypted_response = cipher_suite.encrypt(response.data)
    response.data = encrypted_response
    return response

app.before_request(decrypt_request)
app.after_request(encrypt_response)

# Ruta de ejemplo que simplemente devuelve el contenido del request
@app.route('/example', methods=['POST'])
def example():
    return request.data

if __name__ == '__main__':
    app.run(debug=True)
