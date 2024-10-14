import os
import base64

def base64_to_xlsx(base64_string, output_file):
    # Decodificar el string base64 a bytes
    decoded_data = base64.b64decode(base64_string)

    # Escribir los bytes decodificados en un archivo .xlsx
    with open(output_file, 'wb') as f:
        f.write(decoded_data)

# Ruta del archivo base64 y nombre del archivo .xlsx de salida
file_name = "credentials-config"
archivo_base64 = f"base64/{file_name}.txt"
archivo_xlsx_salida = f"json/{file_name}.json"

# Leer el contenido del archivo base64
with open(archivo_base64, 'r') as f:
    base64_string = f.read()

# Convertir el contenido base64 a un archivo .xlsx
base64_to_xlsx(base64_string, archivo_xlsx_salida)

print("El archivo .xlsx se ha creado con éxito.")
