from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import base64

app = Flask(__name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/encrypt_decrypt', methods=['POST'])
def encrypt_decrypt():
    data = request.get_json()
    operation = data['operation']
    payload = data['payload'].encode()

    if operation == 'encrypt':
        encrypted_payload = cipher_suite.encrypt(payload)
        encrypted_payload = base64.b64encode(encrypted_payload).decode()
        return jsonify({'encrypted_payload': encrypted_payload})

    elif operation == 'decrypt':
        encrypted_payload = base64.b64decode(payload)
        decrypted_payload = cipher_suite.decrypt(encrypted_payload)
        decrypted_payload = decrypted_payload.decode()
        return jsonify({'decrypted_payload': decrypted_payload})

    else:
        return jsonify({'error': 'Invalid operation'}), 400
    

if __name__ == '__main__':
    app.run(debug=True)