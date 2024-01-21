# Importación de dependencias
from datetime import datetime
from business.notification import get_notifications_by_name, create_notification
from models.notification import Notification

datetime_now = datetime.utcnow()

# Ejemplo de uso
new_notification = Notification(name="PruebaSingleton0974", rol="Adminitrador", type="Cargue exitoso", template="Template", description="Notificacion de cargue", status="Activo", created_by="1234", created_at=str(datetime_now), updated_at=str(datetime_now))

# Crear un usuario
create_notification(new_notification)
print(f"Notificación creada: {create_notification}")

# Consultar un usuario por correo
notification_name = "PruebaSingleton"
consulted_notification = get_notifications_by_name(notification_name)

if consulted_notification:
    print(f"Usuario consultado: {consulted_notification}")
else:
    print(f"No se encontró ninguna notificatión con el nombre: {notification_name}")
