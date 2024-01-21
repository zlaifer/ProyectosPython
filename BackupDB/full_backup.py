import os
import psycopg2
from datetime import datetime

def backup_database(database, user, password, host, port, backup_directory):
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        print('Connected to the database')
        
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        
        current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        backup_file = f"{database}_{current_time}.backup"
        
        command = f"pg_dump -Fp -U {user} -W {password} -h {host} -p {port} -f {backup_directory}/{backup_file} {database}"
        print(f"Comando ejecutado => [{command}]")
        
        os.system(command)
        print(f"Backup created at {backup_directory}/{backup_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        if conn:
            conn.close()
            print('Database connection closed.')

backup_database('pgblacklistdb', 'postgres', 'PgBlackList202314', 'localhost', '5432', 'C:\\Users\\haiber.galindo\\Downloads')