import psycopg2
import datetime

# Establecer la conexión a la base de datos
conexion = psycopg2.connect(
    dbname="pgblacklistdb",
    user="postgres",
    password="PgBlackList202314",
    host="localhost",
    port="5432"
)

# # Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# # Crear una tabla
# cursor.execute("""
#     CREATE TABLE mi_tabla (
#         id SERIAL PRIMARY KEY,
#         nombre VARCHAR(50),
#         edad INTEGER
#     )
# """)

# # Guardar los cambios en la base de datos
# conexion.commit()

print(f"<======== Prueba de rendimiento de consulta => [Psycopg2] ========>")

fecha_inicio = datetime.datetime.now()
print(f"Fecha/hora de inicio de la generación de datos => [{fecha_inicio}]")

# Consultar todos los registros de la tabla
cursor.execute("SELECT * FROM test")
registros = cursor.fetchall()

# Imprimir los registros obtenidos
# for registro in registros:
#     print("ID:", registro[0])
#     print("Nombre:", registro[1])
#     print("Edad:", registro[2])
#     print("------------------------")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

fecha_fin = datetime.datetime.now()
diferencia = fecha_fin - fecha_inicio

print(f"Fecha/hora de finalización de la generación de datos => [{fecha_fin}]")
print(f"Total registros consultados => [{len(registros)}] objetos")    
print(f"La consulta de data demoró => [{diferencia.total_seconds()}]")