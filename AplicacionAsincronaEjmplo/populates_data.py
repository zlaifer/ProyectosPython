import psycopg2
import json
import datetime
from faker import Faker

fake = Faker()

DATOS_A_GENERAR = 1000000;

# Database connection
def create_conn():
    conn = psycopg2.connect(
        dbname="pgblacklistdb",
        user="postgres",
        password="PgBlackList202314",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    return conn

# Function to export data
def export_data(table_name):
    conn = create_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Function to export data
def generate_data():
    print("<================================================================>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio de la generación de datos => [{fecha_inicio}]")
    
    datos = []
    for item in range(DATOS_A_GENERAR):
        data = {
            'name': f"{fake.name()}{item}",
            'email': f"{item}{fake.email()}",
            'status': fake.random_element(elements=('ACT', 'INA')),
            'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        datos.append(json.dumps(data))
        
    fecha_fin = datetime.datetime.now()
    diferencia = fecha_fin - fecha_inicio
    
    print(f"Fecha/hora de finlaización de la generación de datos => [{fecha_fin}]")
    print(f"Se generarón => [{len(datos)}] objetos")    
    print(f"La generación de data demoró => [{diferencia.total_seconds()}]")
    print("<================================================================>")
    return datos

# Function to import data
def import_data(table_name, data):
    print("<================================================================>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio de inserción de datos => [{fecha_inicio}]")
    
    conn = create_conn()
    cur = conn.cursor()
    for row in data:
        data_json = json.loads(row)
        query = f"INSERT INTO {table_name} (name, status, created_at, updated_at, email) VALUES (%s, %s, %s, %s, %s)"
        valores = (data_json["name"], data_json["status"], data_json["created_at"], data_json["updated_at"], data_json["email"])
        cur.execute(query, valores)
    conn.commit()
    cur.close()
    conn.close()
    
    fecha_fin = datetime.datetime.now()
    diferencia = fecha_fin - fecha_inicio
    
    print(f"Fecha/hora de finlaización de inserción de datos => [{fecha_inicio}]")
    print(f"La inserción de data demoró => [{diferencia.total_seconds()}]")
    print("<================================================================>")

# Usage
table_name = "test"


# Generate data
generated_data = generate_data()
# print(generated_data)

# # Export data
# exported_data = export_data(table_name)
# print(exported_data)

# Modify data (optional)
# ...

# Import data
import_data(table_name, generated_data)