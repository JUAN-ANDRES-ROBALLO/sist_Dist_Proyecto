from celery import shared_task
import requests
import json

@shared_task
def enviar_notificacion_usuario(cedula, mensaje, tipo):
    """Enviar notificación a un usuario específico"""
    try:
        # Enviar notificación al servicio de notificaciones
        url = 'http://notificaciones:8000/notificaciones/crear/'
        data = {
            'usuario_cedula': cedula,
            'mensaje': mensaje,
            'tipo': tipo
        }
        response = requests.post(url, json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error enviando notificación: {e}")
        return False

@shared_task
def notificar_registro_usuario(cedula, nombre):
    """Notificar cuando se registra un nuevo usuario"""
    mensaje = f"Bienvenido {nombre}! Tu cuenta ha sido creada exitosamente."
    return enviar_notificacion_usuario.delay(cedula, mensaje, 'registro') 