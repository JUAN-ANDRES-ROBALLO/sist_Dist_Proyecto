from celery import shared_task
from .models import Notificacion

@shared_task
def procesar_evento_notificacion(payload):
    tipo = payload.get('tipo')
    usuario_destino = payload.get('usuario')
    contenido = payload.get('contenido')

    if tipo and usuario_destino and contenido:
        Notificacion.objects.create(
            tipo=tipo,
            usuario_destino=usuario_destino,
            contenido=contenido
        )

@shared_task
def eliminar_notificaciones_relacionadas(payload):
    tipo = payload.get('tipo')
    objeto = payload.get('objeto')
    id_afectado = payload.get('id')
    usuario = payload.get('usuario')

    Notificacion.objects.filter(
        tipo='eliminacion',
        usuario_destino=usuario,
        contenido__icontains=f"{objeto}:{id_afectado}"
    ).delete()

