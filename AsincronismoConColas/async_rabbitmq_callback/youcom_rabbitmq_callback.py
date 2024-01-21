from flask import Flask, request
import logging
import pika

app = Flask(__name__)

logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('test.log') # creates handler for the log file
logger.addHandler(handler) # adds handler to the werkzeug WSGI logger

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'queue_messages'
RABBITMQ_EXCHANGE = 'exchange_messages'

# Configuración de conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declaración del exchange
channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='fanout')
# channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='direct')

@app.route('/enqueue', methods=['POST'])
def enqueue():
    message = request.json['message']
    logger.info("Mensaje recibido desde [enqueue]: {}".format(message))
    # Publicar el mensaje en el exchange
    channel.basic_publish(exchange=RABBITMQ_EXCHANGE, routing_key='', body=message)
    return 'Mensaje publicado: {}'.format(message)

def callback(ch, method, properties, body):
    logger.info("<==================================================>")
    logger.info("Mensaje recibido: {}".format(body))
    print("Mensaje recibido: {}".format(body))
    logger.info("<==================================================>")

# Configuración de la cola y la suscripción al exchange
result = channel.queue_declare(queue=RABBITMQ_QUEUE, exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=queue_name)

# Configuración del consumo de mensajes desde la cola
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

if __name__ == '__main__':
    app.run()
