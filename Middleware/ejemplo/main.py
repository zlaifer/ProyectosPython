from flask import Flask, jsonify, request
from command.my_resource import MyResource
from middlewares.handlers import Handlers

app = Flask(__name__)

#Instancia de Handlers
handlers = Handlers()
# Before request handler
app.before_request(handlers.before_request_handler)
# After request handler
app.after_request(handlers.after_request_handler)
# Exception handler
app.errorhandler(handlers.exception_handler)

# Ruta de ejemplo
@app.route('/example', methods=['POST'])
def example():
    print(f'[example][request.json] => [{request.json}]')
    print(f'[example][request.headers] => [{request.headers}]')
    my_resource = MyResource()
    response = my_resource.process_request(request.json)
    return response

if __name__ == '__main__':
    app.run(debug=True)
