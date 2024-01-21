from faker import Faker
import random
import time

# Clase que contiene la logica de las pruebas del servicio
def generacion_data():
    
    # Declaración constantes
    dataFactory = Faker()

    list_roles = ["Administrador", "Auxilar administrativo", "Conductor"]
    list_not_type = ["Cambio de fechas en el Booking", "Cargue exitoso", "La bodega ya puede recibir el contenedor", "Orden cerrada"]
    name = f"Notificación {int(time.time() * 1000)}"
    rol = random.choice(list_roles)
    type = f"Notificación - {random.choice(list_not_type)}"
    template = dataFactory.sentence(nb_words=30)
    description = dataFactory.sentence(nb_words=10)
    created_by = dataFactory.random_int(1000000, 100000000000)
    data = {
                    "data": {
                        "name": f"{name}",
                        "rol": f"{rol}",
                        "type": f"{type}",
                        "template": f"{template}",
                        "description": f"{description}",
                        "created_by": created_by
                    }
                }
            
    print(data)
    
generacion_data()