import psycopg2
from psycopg2 import sql

class SingletonPostgreSQLConnection:
    _instance = None

    def __new__(cls, dbname, user, password, host, port):
        if not cls._instance:
            cls._instance = super(SingletonPostgreSQLConnection, cls).__new__(cls)
            # Crear una conexión a PostgreSQL
            cls._instance.connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )        
        print(cls._instance)
        return cls._instance

    def get_connection(self):
        return self.connection