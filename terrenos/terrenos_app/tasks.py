from celery import shared_task
import requests
import json

@shared_task
def notificar_eliminacion_finca(id_productor, nombre_finca):
    """Notificar cuando se elimina una finca"""
    try:
        url = 'http://notificaciones:8000/notificaciones/crear/'
        data = {
            'usuario_cedula': id_productor,
            'mensaje': f'La finca "{nombre_finca}" ha sido eliminada exitosamente',
            'tipo': 'eliminacion_finca'
        }
        response = requests.post(url, json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error enviando notificación de eliminación de finca: {e}")
        return False

@shared_task
def notificar_eliminacion_parcela(id_productor, nombre_finca, id_parcela):
    """Notificar cuando se elimina una parcela"""
    try:
        url = 'http://notificaciones:8000/notificaciones/crear/'
        data = {
            'usuario_cedula': id_productor,
            'mensaje': f'La parcela {id_parcela} de la finca "{nombre_finca}" ha sido eliminada',
            'tipo': 'eliminacion_parcela'
        }
        response = requests.post(url, json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error enviando notificación de eliminación de parcela: {e}")
        return False 