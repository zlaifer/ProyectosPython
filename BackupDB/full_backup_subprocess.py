""" 
    Se debe garantizar que sea reconocido el comando pg_dump en el sistema,
    por lo que se debe configurar como variable de ambiente
"""

import subprocess

# Set the following variables according to your database and backup configuration
DB_NAME = "pgblacklistdb"
DB_USER = "postgres"
DB_PASSWORD = "PgBlackList202314"
BACKUP_PATH = "/backup"

# Run the pg_dump command to create a full backup of the database
backup_command = f"pg_dump -Fp -U {DB_USER} -W {DB_PASSWORD} -f {BACKUP_PATH}/{DB_NAME}_backup.sql {DB_NAME}"
print(f"Comando ejecutado => [{backup_command}]")

try:
    subprocess.check_output(backup_command, shell=True)
    print(f"Full backup of database {DB_NAME} successfully created.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the full backup of database {DB_NAME}.")
    print(e.output)