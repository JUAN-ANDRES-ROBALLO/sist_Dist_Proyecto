from celery import shared_task

@shared_task
def notificar_nueva_finca(cedula, finca):
    registrar_notificacion.delay(cedula, f'Usuario {cedula} registró la finca {finca}')
# FIXED: This line was breaking Docker due to direct app import
# from notificaciones.api.tasks import registrar_notificacion

@shared_task
def notificar_nueva_finca(cedula, finca):
    registrar_notificacion.delay(cedula, f'Se registró la finca: {finca}')
