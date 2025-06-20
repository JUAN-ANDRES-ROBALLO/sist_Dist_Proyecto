from celery import shared_task

@shared_task
def enviar_evento_eliminacion(tipo, objeto, id_objeto, usuario):
    # Esta función simularía enviar un mensaje a RabbitMQ, en producción usarías publish
    print(f"[EVENTO ENVIADO] tipo: {tipo} | objeto: {objeto} | id: {id_objeto} | usuario: {usuario}")

