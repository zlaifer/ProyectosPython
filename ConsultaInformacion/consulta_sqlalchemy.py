from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
import datetime

CONNECTION_STRING = "postgresql://postgres:PgBlackList202314@localhost:5432/pgblacklistdb"

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


print(f"<======== Prueba de rendimiento de consulta => [SQLAlchemy] ========>")

fecha_inicio = datetime.datetime.now()
print(f"Fecha/hora de inicio de la generación de datos => [{fecha_inicio}]")

# Consultar todos los registros de la tabla
registros = session.query(Test).all()

fecha_fin = datetime.datetime.now()
diferencia = fecha_fin - fecha_inicio

print(f"Fecha/hora de finalización de la generación de datos => [{fecha_fin}]")
print(f"Total registros consultados => [{len(registros)}] objetos")    
print(f"La consulta de data demoró => [{diferencia.total_seconds()}]")

# Imprimir los registros obtenidos
# for registro in registros:
#     print("ID:", registro.id)
#     print("Nombre:", registro.nombre)
#     print("Edad:", registro.edad)
#     print("------------------------")
