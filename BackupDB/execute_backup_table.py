import psycopg2
import os
import shutil

# Replace the placeholders with your actual values
DB_NAME = "pgblacklistdb"
DB_USER = "postgres"
DB_PASSWORD = "PgBlackList202314"
DB_HOST = "localhost"
DB_PORT = "5432"

BACKUP_DIR = "backup"

def backup_database():
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query to fetch the data from the database
    cur.execute("SELECT * FROM test")

    # Fetch all the records from the database
    records = cur.fetchall()

    # Save the fetched data to a backup directory
    with open(os.path.join(BACKUP_DIR, "backup.txt"), "w") as f:
        for record in records:
            f.write(f"{record}\n")

    # Close the cursor and connection
    cur.close()
    conn.close()

# Call the function to back up the database
backup_database()