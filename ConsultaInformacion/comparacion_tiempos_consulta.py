from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
import psycopg2
import datetime

CONNECTION_STRING = "postgresql://postgres:PgBlackList202314@localhost:5432/pgblacklistdb"

TIEMPO_EJECUCION_SQLALCHEMY = None
TIEMPO_EJECUCION_PSYCOPG2 = None

# Crear el motor de la base de datos
engine = create_engine(CONNECTION_STRING)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear una clase para la tabla
Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    email = Column(String)
    

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

def consulta_registros_sqlalchemy():
    print(f"<======== Prueba de rendimiento de consulta => [SQLAlchemy] ========>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio de consulta de datos => [{fecha_inicio}]")
    # Consultar todos los registros de la tabla
    registros = session.query(Test).all()
    fecha_fin = datetime.datetime.now()
    diferencia = fecha_fin - fecha_inicio
    global TIEMPO_EJECUCION_SQLALCHEMY 
    TIEMPO_EJECUCION_SQLALCHEMY = float(diferencia.total_seconds())
    print(f"Fecha/hora de finalización de la generación de datos => [{fecha_fin}]")
    print(f"Total registros consultados => [{len(registros)}] objetos")    
    print(f"La consulta de data demoró => [{TIEMPO_EJECUCION_SQLALCHEMY}]")

def consulta_registros_psycopg2():
    # Establecer la conexión a la base de datos
    conexion = psycopg2.connect(
        dbname="pgblacklistdb",
        user="postgres",
        password="PgBlackList202314",
        host="localhost",
        port="5432"
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()
    print(f"<======== Prueba de rendimiento de consulta => [Psycopg2] ========>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio consulta de datos => [{fecha_inicio}]")
    # Consultar todos los registros de la tabla
    cursor.execute("SELECT * FROM test")
    registros = cursor.fetchall()
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    fecha_fin = datetime.datetime.now()
    diferencia = fecha_fin - fecha_inicio
    global TIEMPO_EJECUCION_PSYCOPG2
    TIEMPO_EJECUCION_PSYCOPG2 = float(diferencia.total_seconds())
    print(f"Fecha/hora de finalización de la generación de datos => [{fecha_fin}]")
    print(f"Total registros consultados => [{len(registros)}] objetos")    
    print(f"La consulta de data demoró => [{TIEMPO_EJECUCION_PSYCOPG2}]")
    

def comparacion():
    iteraciones = 10
    promedio = 0.0
    suma_diferencias = 0.0   
    resumen_iteraciones = []
    for item in range(iteraciones):
        consulta_registros_psycopg2()
        consulta_registros_sqlalchemy()
        diferencia = float(TIEMPO_EJECUCION_SQLALCHEMY - TIEMPO_EJECUCION_PSYCOPG2)
        suma_diferencias += diferencia
        data_iteracion = {
            "iteracion": item+1,
            "tiempo_consulta_sqlalchemy": f"{TIEMPO_EJECUCION_SQLALCHEMY}",
            "tiempo_consulta_psycopg2": f"{TIEMPO_EJECUCION_PSYCOPG2}",
            "diferencia_sqlalchemy_psycopg2": f"{diferencia}"
        }
        resumen_iteraciones.append(data_iteracion)
        # print("\n")
        # print(f"<======== INICIO Comparación tiempos de consulta [1.000.000] registros ========>")
        # print(f"Tiempo de consulta [SQLAlchemy] => [{TIEMPO_EJECUCION_SQLALCHEMY}]")
        # print(f"Tiempo de consulta [Psycopg2] => [{TIEMPO_EJECUCION_PSYCOPG2}]")
        # print(f"Diferencia entre [SQLAlchemy] y [Psycopg2] => [{diferencia}] segundos")
        # print(f"<======== FIN Comparación tiempos de consulta [1.000.000] registros ========>") 
    promedio = suma_diferencias / iteraciones
    resumen = {
        "iteraciones": f"{iteraciones}",
        "suma_diferencias": f"{suma_diferencias}",
        "tiempo_promedio_diferencia": f"{promedio}",
        "resumen_iteraciones": resumen_iteraciones,
    }
    print(resumen)
    
comparacion()