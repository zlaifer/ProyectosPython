from flask import Flask, jsonify, request

app = Flask(__name__)

# Clase con la función que será llamada
class MyResource:
    def process_request(self):
        # Realizar operaciones con el request.json en la función
        return jsonify({'message': 'Función de la clase MyResource', 'data': request.json})

# Middleware before_request
@app.before_request
def before_request():
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
    
# Middleware after_request
@app.after_request
def after_request(response):
    # Puedes realizar operaciones aquí después de que se ha manejado la solicitud.
    # El argumento 'response' es el objeto de respuesta que puedes modificar.
    print("Executing after_request middleware")
    response.headers["after_request"] = True
    return response

# Ruta de ejemplo
@app.route('/example', methods=['POST'])
def example():
    print(f'[example][request.json] => [{request.json}]')
    print(f'[example][request.headers] => [{request.headers}]')
    my_resource = MyResource()
    response = my_resource.process_request()
    return response

if __name__ == '__main__':
    app.run(debug=True)
