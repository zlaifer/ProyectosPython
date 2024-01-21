from flask import Flask, request
import pika

app = Flask(__name__)

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = '/'

@app.route('/enqueue', methods=['POST'])
def enqueue_message():
    message = request.json['message']
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)
    connection.close()
    return 'Message enqueued successfully.'

@app.route('/dequeue', methods=['GET'])
def dequeue_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    method_frame, header_frame, body = channel.basic_get(queue=RABBITMQ_QUEUE)
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)
        connection.close()
        return body.decode()
    else:
        connection.close()
        return 'No messages in the queue.'

if __name__ == '__main__':
    app.run()
