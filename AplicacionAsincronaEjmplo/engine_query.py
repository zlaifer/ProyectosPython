import psycopg2
import datetime
import pika
import json
import time

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'queue_messages'

def proceso_batch():
    print("<================================================================>")
    fecha_inicio = datetime.datetime.now()
    print(f"Fecha/hora de inicio del Motor de Consulta => [{fecha_inicio}]")
    
    # Conexión a la base de datos PostgreSQL
    conn = psycopg2.connect(
        dbname="pgblacklistdb",
        user="postgres",
        password="PgBlackList202314",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Consulta de información de la base de datos
    cursor.execute("SELECT id, name, status, created_at, updated_at, email FROM test WHERE status = 'ACT' LIMIT 20");
    resultados = cursor.fetchall()

    # Cierre de la conexión a la base de datos
    cursor.close()
    conn.close()
    
    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Envío de información a la cola RabbitMQ
    for resultado in resultados:        
        # Convierte los datos en JSON
        data_json = {
            "id": resultado[0],
            "name": resultado[1],
            "status": resultado[2],
            "created_at": f"{resultado[3].strftime('%Y-%m-%d %H:%M:%S')}",
            "updated_at": f"{resultado[4].strftime('%Y-%m-%d %H:%M:%S')}",
            "email": resultado[5]
        }
        # Publicar el mensaje en la cola
        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=json.dumps(data_json))

    # Cierre de la conexión a la cola RabbitMQ
    connection.close()

    fecha_fin = datetime.datetime.now()
    print(f"Se enviarón => [{len(resultados)}] mensajes a la cola [{RABBITMQ_QUEUE}]")    
    diferencia = fecha_fin - fecha_inicio
    print(f"El procesamiento tardó => [{diferencia.total_seconds()}] segundos")
    print(f"Fecha/hora de finlaización del Motor de Consulta => [{fecha_fin}]")
    print("<================================================================>")

while True:
    proceso_batch()
    time.sleep(180)  # Espera 5 minutos antes de ejecutar el proceso nuevamente
