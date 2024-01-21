# Modelo de Notificaciones
class Notification:
    def __init__(self, name, rol, type, template, description, status, created_by, created_at, updated_at):
        self.name = name
        self.rol = rol
        self.type = type
        self.template = template
        self.description = description
        self.status = status
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"Notification(name={self.name}, rol={self.rol}, type={self.type}, template={self.template}, description={self.description}, status={self.status}, created_by={self.created_by}, created_at={self.created_at}, updated_at={self.updated_at})"