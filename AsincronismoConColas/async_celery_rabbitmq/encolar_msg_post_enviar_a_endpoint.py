from flask import Flask, request
from celery import Celery
import requests

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def process_message(message):
    # Envía el message al endpoint preestablecido
    endpoint = 'http://localhost:5000/callback'
    response = requests.post(endpoint, json={'message': message})
    return response.status_code

@app.route('/enqueue', methods=['POST'])
def encolar():
    message = request.json['message']
    process_message.delay(message)  # Encola el message para su envío al endpoint
    return 'message encolado'

@app.route('/callback', methods=['POST'])
def callback():
    message = request.json
    print(message)
    return message

if __name__ == '__main__':
    app.run()
