from celery import shared_task
import requests
import json

@shared_task
def notificar_venta_maquinaria(propietario_cedula, id_maquinaria, precio):
    """Notificar cuando se publica una venta de maquinaria"""
    try:
        url = 'http://notificaciones:8000/notificaciones/crear/'
        data = {
            'usuario_cedula': propietario_cedula,
            'mensaje': f'Tu maquinaria {id_maquinaria} ha sido publicada para venta por ${precio}',
            'tipo': 'venta_maquinaria'
        }
        response = requests.post(url, json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error enviando notificación de venta: {e}")
        return False

@shared_task
def notificar_reserva_maquinaria(propietario_cedula, id_maquinaria, fecha_inicio, fecha_fin):
    """Notificar cuando se publica una reserva de maquinaria"""
    try:
        url = 'http://notificaciones:8000/notificaciones/crear/'
        data = {
            'usuario_cedula': propietario_cedula,
            'mensaje': f'Tu maquinaria {id_maquinaria} ha sido publicada para reserva del {fecha_inicio} al {fecha_fin}',
            'tipo': 'reserva_maquinaria'
        }
        response = requests.post(url, json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error enviando notificación de reserva: {e}")
        return False

@shared_task
def notificar_interes_compra(propietario_cedula, id_maquinaria, comprador_cedula):
    """Notificar al propietario cuando alguien está interesado en comprar"""
    try:
        url = 'http://notificaciones:8000/notificaciones/crear/'
        data = {
            'usuario_cedula': propietario_cedula,
            'mensaje': f'El usuario {comprador_cedula} está interesado en comprar tu maquinaria {id_maquinaria}',
            'tipo': 'interes_compra'
        }
        response = requests.post(url, json=data)
        return response.status_code == 201
    except Exception as e:
        print(f"Error enviando notificación de interés: {e}")
        return False 