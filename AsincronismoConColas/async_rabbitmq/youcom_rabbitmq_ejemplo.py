from flask import Flask, request
import pika

app = Flask(__name__)

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = '/'

@app.route('/enqueue', methods=['POST'])
def enviar_mensaje():
    mensaje = request.json['message']

    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declarar la cola
    channel.queue_declare(queue=RABBITMQ_QUEUE)

    # Publicar el mensaje en la cola
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=mensaje)

    # Cerrar la conexión
    connection.close()

    return 'Mensaje enviado'

@app.route('/dequeue', methods=['GET'])
def recibir_mensaje():
    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar la cola
    channel.queue_declare(queue=RABBITMQ_QUEUE)

    # Consumir mensajes de la cola
    method_frame, header_frame, body = channel.basic_get(queue=RABBITMQ_QUEUE, auto_ack=True)

    # Cerrar la conexión
    connection.close()

    return body.decode() if body else 'No hay mensajes'

if __name__ == '__main__':
    app.run()
