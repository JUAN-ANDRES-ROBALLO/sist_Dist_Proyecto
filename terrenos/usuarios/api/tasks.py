from notificaciones.api.tasks import registrar_notificacion
from celery import shared_task

@shared_task
def enviar_bienvenida(cedula):
    registrar_notificacion.delay(cedula, f'Bienvenido {cedula}, tu cuenta ha sido registrada.')