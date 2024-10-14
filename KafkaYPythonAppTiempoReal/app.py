from flask import Flask, render_template
from flask_socketio import SocketIO
from confluent_kafka import Consumer, KafkaError
import json


"""
ChatGPT
Para implementar un caso de uso con Kafka y Python donde se visualice información en tiempo real en una página HTML, 
puedes utilizar Flask para crear un servidor web simple y utilizar la biblioteca de JavaScript llamada Socket.IO 
para la comunicación bidireccional entre el servidor y el cliente. En este ejemplo, asumiré que ya has configurado Apache Kafka 
y tienes un tópico llamado mi_tema al que se enviarán los mensajes.
"""

app = Flask(__name__)
socketio = SocketIO(app)

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  # Dirección del servidor Kafka
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
}

# Crear un consumidor
consumer = Consumer(config)

# Tópico al que se suscribirá el consumidor
topic = 'mi_tema'

# Suscribirse al tópico
consumer.subscribe([topic])

# Función para emitir mensajes a través de Socket.IO
def send_message(message):
    socketio.emit('mensaje', message)

# Función para manejar la recepción de mensajes
def handle_messages():
    while True:
        msg = consumer.poll(1.0)  # Esperar 1 segundo por mensajes

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        # Enviar el mensaje al cliente a través de Socket.IO
        send_message(msg.value().decode('utf-8'))

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Iniciar la función de manejo de mensajes en un hilo separado
socketio.start_background_task(target=handle_messages)

if __name__ == '__main__':
    socketio.run(app)
