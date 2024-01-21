# Importación de dependencias
from models.notification import Notification
from models.SingletonPostgreSQLConnection import SingletonPostgreSQLConnection, sql

# Uso del SingletonPostgreSQLConnection
dbname = "notificationsdb"
user = "admin"
password = "admin"
host = "localhost"
port = "5432"

# Obtener la instancia única de la conexión
connection_instance = SingletonPostgreSQLConnection(dbname, user, password, host, port).get_connection()

# Crear un usuario
def create_notification(notification):
    with connection_instance.cursor() as cursor:
        query = sql.SQL("INSERT INTO notifications (name, rol, type, template, description, status, created_by, created_at, updated_at) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {});").format(
            sql.Literal(notification.name), sql.Literal(notification.rol), sql.Literal(notification.type), sql.Literal(notification.template), sql.Literal(notification.description), sql.Literal(notification.status), sql.Literal(notification.created_by), sql.Literal(notification.created_at), sql.Literal(notification.updated_at)
        )
        cursor.execute(query)
    connection_instance.commit()

# Consultar un usuario
def get_notifications_by_name(id):
    # Obtener la instancia única de la conexión
    connection_instance = SingletonPostgreSQLConnection(dbname, user, password, host, port).get_connection()
    with connection_instance.cursor() as cursor:
        query = sql.SQL("SELECT * FROM notifications WHERE name = {};").format(sql.Literal(id))
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return Notification(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9])
        else:
            return None

