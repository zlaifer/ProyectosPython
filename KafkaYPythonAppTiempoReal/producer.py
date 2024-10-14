from confluent_kafka import Producer
import json
import time

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Dirección del servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# Tópico al que se enviarán los mensajes
topic = 'mi_tema'

# Función para manejar la entrega de mensajes
def delivery_report(err, msg):
    if err is not None:
        print('Error al enviar el mensaje:', err)
    else:
        print('Mensaje enviado al tópico {} [{}]'.format(msg.topic(), msg.partition()))

# Enviar mensajes al tópico cada segundo
while True:
    message = {'key': '1', 'value': 'Mensaje en tiempo real: {}'.format(time.strftime('%H:%M:%S'))}
    producer.produce(topic, key=json.dumps(message['key']), value=json.dumps(message['value']), callback=delivery_report)
    producer.flush()
    time.sleep(1)
