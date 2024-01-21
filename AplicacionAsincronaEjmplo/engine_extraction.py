import psycopg2
import datetime
import pika
import json

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'queue_messages'

# Database connection
def create_conn():
    conn = psycopg2.connect(
        dbname="pgblacklistdb",
        user="postgres",
        password="PgBlackList202314",
        host="localhost",
        port="5432"
    )
    return conn

def callback(ch, method, properties, body):
    print("<================================================================>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio del Motor de Extracción => [{fecha_inicio}]")
    # Aquí va el código que se ejecutará cuando se reciba un mensaje en la cola
    print("Mensaje recibido:", body)
    data_json = json.loads(body)
    
    conn = create_conn()
    cur = conn.cursor()
    # Realizar el procesamiento del mensaje aquí
    query_update = f"UPDATE test SET status='ACT_MOD' WHERE id={data_json['id']}"
    cur.execute(query_update)
    conn.commit()
    cur.close()
    conn.close()
    
    # Confirmar el procesamiento del mensaje
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
    fecha_fin = datetime.datetime.now()
    diferencia = fecha_fin - fecha_inicio
    print(f"Fecha/hora de finlaización del Motor de Extracción => [{fecha_fin}]")
    print(f"La actualización de data demoró => [{diferencia.total_seconds()}]")
    print("<================================================================>")

# Establecer conexión con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()

# Declarar la cola y asociar el callback a la cola
channel.queue_declare(queue=RABBITMQ_QUEUE)
channel.basic_qos(prefetch_count=1)  # Limitar a un mensaje sin confirmar a la vez
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

# Iniciar la escucha de mensajes
print('Esperando mensajes. Presiona CTRL+C para salir ...')
channel.start_consuming()
