# maquinaria/app/tasks.py
from celery import shared_task
import json
import pika

@shared_task
def enviar_notificacion_rabbitmq(payload):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='notificaciones_compras_servicios')
        channel.basic_publish(
            exchange='',
            routing_key='notificaciones_compras_servicios',
            body=json.dumps(payload)
        )
        connection.close()
        return f"Mensaje enviado: {payload}"
    except Exception as e:
        return f"Error al enviar mensaje: {str(e)}"

