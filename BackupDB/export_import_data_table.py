import psycopg2

# Database connection
def create_conn():
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
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

# Function to import data
def import_data(table_name, data):
    conn = create_conn()
    cur = conn.cursor()
    for row in data:
        placeholders = ', '.join(['%s'] * len(row))
        columns = ', '.join(row.keys())
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cur.execute(insert_query, list(row.values()))
    conn.commit()
    cur.close()
    conn.close()

# Usage
table_name = "your_table_name"

# Export data
exported_data = export_data(table_name)

# Modify data (optional)
# ...

# Import data
import_data(table_name, exported_data)