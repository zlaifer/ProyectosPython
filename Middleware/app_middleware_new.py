from flask import Flask, request, jsonify

app = Flask(__name__)

# Middleware para eliminar la clave "data" del request.json
class RemoveDataMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        with self.app.request_context(environ):
            try:
                # Manipular el request antes de llegar a la función
                if request.method == 'POST' and request.is_json:
                    # Verificar si existe la clave "data" en request.json
                    if 'data' in request.json:
                        print(request.json)
                        # Eliminar la clave "data"
                        request_data = request.json.pop('data')
                        print(request_data)
                        # Actualizar el contenido de la solicitud con el JSON modificado
                        request.data = request.get_data()
                        request._cached_json = None
                        request._cached_json_data = None
            except Exception as e:
                response = jsonify({'error': f'Error al manipular request.json: {str(e)}'})
                return response(environ, start_response)

            # Llamar a la aplicación principal
            app_iter = self.app(environ, start_response)

            return app_iter

app.wsgi_app = RemoveDataMiddleware(app)

# Ruta de ejemplo que muestra el request.json modificado
@app.route('/example', methods=['POST'])
def example():
    return jsonify(request.json)

if __name__ == '__main__':
    app.run(debug=True)
