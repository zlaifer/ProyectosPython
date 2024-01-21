# Importacion de dependencias
from flask import  request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


# Clave para encriptar y desencriptar
# SECRET_KEY = Fernet.generate_key() # Cambia esto por una clave segura y guárdala de forma segura
with open('clave.txt', 'rb') as key_file:
    SECRET_KEY = key_file.read()
        
# Función para encriptar datos
def encrypt(data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    encrypted_data = b64encode(cipher_text).decode('utf-8')
    return {'iv': iv, 'encrypted_data': encrypted_data}

# Función para desencriptar datos
def decrypt(data):
    iv = b64decode(data['iv'])
    cipher_text = b64decode(data['encrypted_data'])
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipher_text), AES.block_size).decode('utf-8')
    return decrypted_data

# Decorador para desencriptar el request y encriptar el response
def encrypt_decrypt_decorator(func):
    def wrapper(*args, **kwargs):
        # Desencriptar el request si es necesario
        if request.data:
            decrypted_data = decrypt(request.json)
            request.data = decrypted_data

        # Llamar a la función de vista
        response = func(*args, **kwargs)

        # Encriptar el response si es necesario
        if response.data:
            encrypted_data = encrypt(response.data)
            response.data = jsonify(encrypted_data)

        return response

    return wrapper
