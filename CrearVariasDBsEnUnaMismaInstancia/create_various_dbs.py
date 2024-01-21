from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la instancia de la base de datos principal
engine = create_engine('postgresql://postgres:PgBlackList202314@localhost:5432/pgblacklistdb')
Session = sessionmaker(bind=engine)
session = Session()
# Habilitamos AUTOCOMMIT 
session.connection().connection.set_isolation_level(0)

# Crear la clase base declarativa
Base = declarative_base(bind=engine)


# Definir las tablas de la base de datos principal
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

# Crear la base de datos principal y sus tablas
Base.metadata.create_all()

# Crear las bases de datos secundarias y sus tablas
db_names = ['database1', 'database2', 'database3']

for db_name in db_names:
    # Crear la base de datos secundaria
    session.execute(f'CREATE DATABASE {db_name}')

    # Crear la instancia de la base de datos secundaria
    engine_secondary = create_engine(f'postgresql://postgres:PgBlackList202314@localhost:5432/{db_name}')
    Session_secondary = sessionmaker(bind=engine_secondary)
    session_secondary = Session_secondary()

    # Crear la clase base declarativa para la base de datos secundaria
    Base_secondary = declarative_base(bind=engine_secondary)

    # Definir las tablas de la base de datos secundaria
    class Item(Base_secondary):
        __tablename__ = 'items'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        price = Column(Integer)

    # Crear las tablas de la base de datos secundaria
    Base_secondary.metadata.create_all()

    # Cerrar la sesión de la base de datos secundaria
    session_secondary.close()
