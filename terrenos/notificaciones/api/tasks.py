from celery import shared_task
from .models import Notificacion

@shared_task
def registrar_notificacion(cedula, mensaje):
    Notificacion.objects.create(propietario=cedula, descripcion=mensaje)
