from flask import jsonify, request


class Handlers:
    def before_request_handler(self):
        # Puedes realizar operaciones aquí antes de que se maneje la solicitud
        # Este código se ejecutará antes de cada solicitud.
        print("Executing before_request middleware")
        print(request.json)
        if 'data' in request.json:
            # Obtener la información dentro de 'data'
            original_json = request.json["data"]
            # Eliminar la clave 'data', que al ser el padre deje el objeto vacio {}
            request.json.pop('data')
            # Remplazamo el request por el objeto sin el 'data'
            for key, value in original_json.items():
                request.json[key] = value
        print(original_json)

    def after_request_handler(self, response):
        # Puedes realizar operaciones aquí después de que se ha manejado la solicitud.
        # El argumento 'response' es el objeto de respuesta que puedes modificar.
        print("Executing after_request middleware")
        response.headers["after_request"] = True
        return response
    
    def exception_handler(err):
        response = {
            "description": err.description
        }
        return jsonify(response), err.code