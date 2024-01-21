from flask import Flask, request
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def process_message(message):
    # Procesa el mensaje aquí
    return f'Procesado: {message}'

@app.route('/enqueue', methods=['POST'])
def encolar():
    message = request.json['message']
    process_message.delay(message)  # Encola el mensaje para su procesamiento
    return 'Mensaje encolado'

@app.route('/dequeue', methods=['GET'])
def desencolar():
    result = process_message.delay('')  # Desencola un mensaje
    return result.get()

if __name__ == '__main__':
    app.run()
