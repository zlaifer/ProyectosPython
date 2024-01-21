from Crypto.PublicKey import RSA

# Generar un nuevo par de claves RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Guardar la clave pública en un archivo
with open("./keys/public.pem", "wb") as f:
    f.write(public_key)

# Guardar la clave privada en un archivo
with open("./keys/private.pem", "wb") as f:
    f.write(private_key)
