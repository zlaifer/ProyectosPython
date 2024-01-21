# Clase con la función que será llamada
from flask import jsonify

class MyResource:
    def process_request(self, data):
        # Realizar operaciones con el request.json en la función
        return jsonify({'message': 'Función de la clase MyResource', 'data': data})