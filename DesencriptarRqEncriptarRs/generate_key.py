from cryptography.fernet import Fernet

# Clave para encriptar y desencriptar
SECRET_KEY = Fernet.generate_key() # Cambia esto por una clave segura y guárdala de forma segura

# Escribir la clave en un archivo
with open('clave.txt', 'wb') as key_file:
    key_file.write(SECRET_KEY)