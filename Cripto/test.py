from cryptography.fernet import Fernet

def cifrar_texto(texto, clave):
    cipher_suite = Fernet(clave)
    texto_cifrado = cipher_suite.encrypt(texto.encode())
    return texto_cifrado

TEXT_TO_ENCRYPT = 'epdu gaor vyba btyl'
KEY = 'U_OdJzH54I7cMdIwfwcPz4zQihMj9SiXewe_nsRSB0E='

print(cifrar_texto(TEXT_TO_ENCRYPT, KEY))

TEXT_TO_ENCRYPT = 'miso.pruebas.2023@gmail.com'
KEY = 'U_OdJzH54I7cMdIwfwcPz4zQihMj9SiXewe_nsRSB0E='

print(cifrar_texto(TEXT_TO_ENCRYPT, KEY))