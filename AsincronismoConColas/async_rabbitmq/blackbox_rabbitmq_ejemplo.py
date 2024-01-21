from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = '/'

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declare a queue to send messages to
channel.queue_declare(queue=RABBITMQ_QUEUE)

@app.route('/enqueue', methods=['POST'])
def enqueue():
    message = request.json['message']
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)
    return jsonify({'status': 'success'})

@app.route('/dequeue', methods=['GET'])
def dequeue():
    method_frame, header_frame, body = channel.basic_get(queue=RABBITMQ_QUEUE)
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)
        return jsonify({'message': body.decode()})
    else:
        return jsonify({'status': 'No messages available'})

if __name__ == '__main__':
    app.run(debug=True)