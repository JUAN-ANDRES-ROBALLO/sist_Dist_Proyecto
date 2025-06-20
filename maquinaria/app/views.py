import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria

# Ver página principal
def maquinaria_home(request):
    return render(request, 'maquinaria/maquinaria.html')

# Formulario agregar maquinaria
def form_agregar_maquinaria(request):
    return render(request, 'maquinaria/form_agregar_maquinaria.html')

# Lista maquinaria propia
def listar_mi_maquinaria(request):
    cedula = request.session.get("usuario")
    maquinaria = Maquinaria.objects.filter(propietario__cedula=cedula)
    data = list(maquinaria.values())
    return JsonResponse({"maquinaria": data})

@csrf_exempt
def agregar_maquinaria(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cedula = request.session.get("usuario")
        m = Maquinaria(
            tipo=data["tipo"],
            marca=data["marca"],
            modelo=data["modelo"],
            anio=data["anio"],
            propietario_id=cedula
        )
        m.save()
        return JsonResponse({"success": "Maquinaria agregada"})
    return JsonResponse({"error": "Método inválido"}, status=400)

@csrf_exempt
def eliminar_maquinaria(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            m = Maquinaria.objects.get(id_maquinaria=data["id"], propietario__cedula=request.session.get("usuario"))
            m.delete()
            return JsonResponse({"success": "Maquinaria eliminada"})
        except Maquinaria.DoesNotExist:
            return JsonResponse({"error": "No existe o no autorizado"}, status=404)
    return JsonResponse({"error": "Método inválido"}, status=400)

from django.utils import timezone
from django.views.decorators.http import require_http_methods
import datetime

@csrf_exempt
def poner_en_venta(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cedula = request.session.get("usuario")
        try:
            maquinaria = Maquinaria.objects.get(id_maquinaria=data["id"], propietario__cedula=cedula)
            VentaMaquinaria.objects.create(
                maquinaria=maquinaria,
                propietario_id=cedula,
                precio=data["precio"]
            )
            return JsonResponse({"success": "Publicada en venta"})
        except Maquinaria.DoesNotExist:
            return JsonResponse({"error": "No autorizada"}, status=403)

@csrf_exempt
def sacar_de_venta(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cedula = request.session.get("usuario")
        try:
            venta = VentaMaquinaria.objects.get(maquinaria__id_maquinaria=data["id"], propietario__cedula=cedula)
            venta.delete()
            return JsonResponse({"success": "Eliminada de venta"})
        except VentaMaquinaria.DoesNotExist:
            return JsonResponse({"error": "No encontrada en venta"}, status=404)

@csrf_exempt
def poner_en_servicio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cedula = request.session.get("usuario")
        try:
            maquinaria = Maquinaria.objects.get(id_maquinaria=data["id"], propietario__cedula=cedula)
            ReservaMaquinaria.objects.create(
                maquinaria=maquinaria,
                propietario_id=cedula,
                fecha_inicio=None,
                fecha_fin=None
            )
            return JsonResponse({"success": "Puesta en servicio"})
        except Maquinaria.DoesNotExist:
            return JsonResponse({"error": "No autorizada"}, status=403)

@csrf_exempt
def sacar_de_servicio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cedula = request.session.get("usuario")
        try:
            reserva = ReservaMaquinaria.objects.get(maquinaria__id_maquinaria=data["id"], propietario__cedula=cedula)
            reserva.delete()
            return JsonResponse({"success": "Eliminada de servicio"})
        except ReservaMaquinaria.DoesNotExist:
            return JsonResponse({"error": "No encontrada"}, status=404)

import pika  # Para enviar mensajes a RabbitMQ

@csrf_exempt
def maquinaria_en_venta(request):
    # Mostrar toda maquinaria en venta excepto la del usuario logueado
    user_id = request.session.get("usuario")
    publicaciones = VentaMaquinaria.objects.exclude(propietario__cedula=user_id).select_related("maquinaria", "propietario")
    data = [
        {
            "id": pub.maquinaria.id_maquinaria,
            "tipo": pub.maquinaria.tipo,
            "marca": pub.maquinaria.marca,
            "modelo": pub.maquinaria.modelo,
            "anio": pub.maquinaria.anio,
            "precio": float(pub.precio),
            "vendedor": pub.propietario.nombre,
            "email": pub.propietario.email
        }
        for pub in publicaciones
    ]
    return JsonResponse({"ventas": data})


@csrf_exempt
def comprar_maquinaria(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comprador_id = request.session.get("usuario")
        try:
            venta = VentaMaquinaria.objects.get(maquinaria__id_maquinaria=data["id"])
            if venta.propietario.cedula == comprador_id:
                return JsonResponse({"error": "No podés comprar tu propia maquinaria"}, status=403)
            
            comprador = venta.maquinaria.propietario  # o buscar Usuario.objects.get(cedula=comprador_id)
            
            # Notificación por RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            channel = connection.channel()
            channel.queue_declare(queue='notificaciones_compras_servicios')
            payload = {
                "tipo": "compra",
                "maquinaria_id": venta.maquinaria.id_maquinaria,
                "vendedor": venta.propietario.email,
                "comprador": comprador.email,
                "nombre_comprador": comprador.nombre
            }
            channel.basic_publish(
                exchange='',
                routing_key='notificaciones_compras_servicios',
                body=json.dumps(payload)
            )
            connection.close()
            return JsonResponse({"success": "Notificación enviada al vendedor"})
        except VentaMaquinaria.DoesNotExist:
            return JsonResponse({"error": "No encontrada"}, status=404)


@csrf_exempt
def maquinaria_en_servicio(request):
    # Mostrar reservas en servicio excepto las del usuario logueado
    user_id = request.session.get("usuario")
    publicaciones = ReservaMaquinaria.objects.exclude(propietario__cedula=user_id).select_related("maquinaria", "propietario")
    data = [
        {
            "id": pub.maquinaria.id_maquinaria,
            "tipo": pub.maquinaria.tipo,
            "marca": pub.maquinaria.marca,
            "modelo": pub.maquinaria.modelo,
            "anio": pub.maquinaria.anio,
            "fecha_inicio": str(pub.fecha_inicio) if pub.fecha_inicio else None,
            "fecha_fin": str(pub.fecha_fin) if pub.fecha_fin else None,
            "vendedor": pub.propietario.nombre,
            "email": pub.propietario.email
        }
        for pub in publicaciones
    ]
    return JsonResponse({"servicios": data})


@csrf_exempt
def pedir_maquinaria(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comprador_id = request.session.get("usuario")
        try:
            reserva = ReservaMaquinaria.objects.get(maquinaria__id_maquinaria=data["id"])
            if reserva.propietario.cedula == comprador_id:
                return JsonResponse({"error": "No podés pedir tu propia maquinaria"}, status=403)

            # Validar fechas
            fecha_inicio = datetime.datetime.strptime(data["fecha_inicio"], "%Y-%m-%d").date()
            fecha_fin = datetime.datetime.strptime(data["fecha_fin"], "%Y-%m-%d").date()
            hoy = timezone.now().date()
            if fecha_inicio < hoy or fecha_fin < fecha_inicio:
                return JsonResponse({"error": "Fechas inválidas"}, status=400)

            reserva.fecha_inicio = fecha_inicio
            reserva.fecha_fin = fecha_fin
            reserva.save()

            comprador = reserva.maquinaria.propietario

            # Enviar notificación RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            channel = connection.channel()
            channel.queue_declare(queue='notificaciones_compras_servicios')
            payload = {
                "tipo": "pedido",
                "maquinaria_id": reserva.maquinaria.id_maquinaria,
                "vendedor": reserva.propietario.email,
                "comprador": comprador.email,
                "nombre_comprador": comprador.nombre,
                "fecha_inicio": str(fecha_inicio),
                "fecha_fin": str(fecha_fin)
            }
            channel.basic_publish(
                exchange='',
                routing_key='notificaciones_compras_servicios',
                body=json.dumps(payload)
            )
            connection.close()
            return JsonResponse({"success": "Notificación enviada al dueño"})
        except ReservaMaquinaria.DoesNotExist:
            return JsonResponse({"error": "No encontrada"}, status=404)

