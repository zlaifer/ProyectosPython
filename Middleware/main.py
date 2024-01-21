from flask import Flask, request, jsonify
from errors import ApiError
from middlewares import validation_and_response_middleware

app = Flask(__name__)

# Aplicar el decorador a rutas específicas
@app.route('/example', methods=['POST'], endpoint='example')
@validation_and_response_middleware
def example():
    # Obtener datos de la solicitud
    data = request.json if request.json else {}

    # Responder con datos y el middleware añadirá información adicional al response
    
    return jsonify(data["data"])

@app.route('/example/<int:exampleId>', methods=['GET'], endpoint='example_get')
@validation_and_response_middleware
def example_get(exampleId):
    # Obtener datos de la solicitud
    data = request.json if request.json else {}

    # Responder con datos y el middleware añadirá información adicional al response
    data =  {
                "id": exampleId,
                "created_by": 123,
                "description": "adfkjasdkfjasldkfjaslkdfj",
                "name": "Notificacion cargue exitoso vehiculo 4140",
                "rol": "Administrador",
                "template": "lkadsjflkajsdfajdf",
                "type": "Notificacion de prueba"
            }
    return jsonify(data)

# Middleware para manejar los errores
@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "description": err.description
    }
    return jsonify(response), err.code

if __name__ == '__main__':
    app.run(debug=True)