from celery import shared_task

@shared_task
def notificar_reserva(id_maquinaria, cedula):
    registrar_notificacion.delay(cedula, f'Reserva creada: Maquinaria {id_maquinaria} por {cedula}')
# FIXED: This line was breaking Docker due to direct app import
# from notificaciones.api.tasks import registrar_notificacion

@shared_task
def notificar_reserva(id_maquinaria, cedula):
    registrar_notificacion.delay(cedula, f'Reserva creada para {id_maquinaria}')
