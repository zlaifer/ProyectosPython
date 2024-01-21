from flask import request, jsonify
from errors import ApiError
from validators import validate_schema, update_notification_schema

# Middleware para validar el request y manipular el response
def validation_and_response_middleware(func):
    def wrapper(*args, **kwargs):
        # Validar el request si es necesario
        if request.method in ['POST', 'PUT', 'PATCH']:
            data = request.get_json()
            print(data)
            data = data["data"] 
            validate_schema(data, update_notification_schema)
        
        # Llamar a la función de vista
        response = func(*args, **kwargs)

        # Manipular el response añadiendo información adicional
        if response.is_json:
            data = response.get_json()
            # data['additional_info'] = 'Información adicional en el response'
            if request.method == 'POST':
                response = {"data": data}, 201
            else:
                response = {"data": data}

        return response

    return wrapper

