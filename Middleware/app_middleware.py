from flask import Flask, request, jsonify

app = Flask(__name__)

# Middleware para manipular el request y el response
class RequestResponseMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Manipular el request antes de llegar a la función
        if request.method == 'POST':
            try:
                # Agregar información al request.json
                request.json['new_key'] = 'new_value'
            except Exception as e:
                return jsonify({'error': f'Error al manipular request.json: {str(e)}'}), 400

        # Llamar a la aplicación principal
        app_iter = self.app(environ, start_response)

        # Manipular el response después de la función
        if 'Content-Length' in start_response.headers:
            response_data = b''.join(app_iter)
            try:
                # Modificar el contenido del response
                modified_response_data = response_data.upper()
                start_response.headers['Content-Length'] = str(len(modified_response_data))
                return [modified_response_data]
            except Exception as e:
                return jsonify({'error': f'Error al manipular el response: {str(e)}'}), 500

        return app_iter

# app.wsgi_app = RequestResponseMiddleware(app.wsgi_app)

# Clase con la función que será llamada
class MyResource:
    def process_request(self):
        # Realizar operaciones con el request.json en la función
        return jsonify({'message': 'Función de la clase MyResource', 'data': request.json})

# Instancia de la clase
# my_resource = MyResource()

# Ruta de ejemplo que llama a la función de la clase MyResource
@app.route('/example', methods=['POST'])
def example():
    # Llamar a la función de la clase MyResource
    my_resource = MyResource()
    response = my_resource.process_request()

    return response

if __name__ == '__main__':
    app.run(debug=True)
