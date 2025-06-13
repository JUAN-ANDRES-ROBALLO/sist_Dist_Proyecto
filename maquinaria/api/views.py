from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria, Contador
from .serializers import MaquinariaSerializer, VentaMaquinariaSerializer, ReservaMaquinariaSerializer
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Helpers

def obtener_contador(nombre):
    contador, created = Contador.objects.get_or_create(nombre=nombre, defaults={'valor': 0})
    contador.valor += 1
    contador.save()
    return contador.valor

# Maquinaria

@csrf_exempt
@api_view(['GET', 'POST'])
def maquinaria_list_create(request):
    if request.method == 'GET':
        user_token = request.headers.get('X-User-Token')
        maquinaria = Maquinaria.objects.filter(id_maquinaria__in=[
            m.id_maquinaria for m in Maquinaria.objects.all() if
            VentaMaquinaria.objects.filter(id_maquinaria=m).exists() == False and
            ReservaMaquinaria.objects.filter(id_maquinaria=m).exists() == False and
            m.id_maquinaria in [x.id_maquinaria for x in Maquinaria.objects.filter(id_maquinaria__in=[m.id_maquinaria for m in Maquinaria.objects.all() if m.id_maquinaria[:len(user_token)] == user_token])]
        ])
        maquinaria = Maquinaria.objects.filter(id_maquinaria__startswith=user_token)
        serializer = MaquinariaSerializer(maquinaria, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        next_id = obtener_contador('id_maquinaria')
        id_maquinaria = f'MAQ{next_id:05d}'

        data = request.data.copy()
        data['id_maquinaria'] = id_maquinaria

        serializer = MaquinariaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def maquinaria_delete(request, id_maquinaria):
    try:
        maq = Maquinaria.objects.get(id_maquinaria=id_maquinaria)
        maq.delete()
        return Response({'message': 'Maquinaria eliminada.'}, status=status.HTTP_200_OK)
    except Maquinaria.DoesNotExist:
        return Response({'error': 'Maquinaria no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

# Venta

@csrf_exempt
@api_view(['GET', 'POST'])
def venta_list_create(request):
    if request.method == 'GET':
        venta = VentaMaquinaria.objects.all()
        serializer = VentaMaquinariaSerializer(venta, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        next_id = obtener_contador('id_listado_v')
        id_listado_v = f'VEN{next_id:05d}'

        data = request.data.copy()
        data['id_listado_v'] = id_listado_v

        serializer = VentaMaquinariaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def venta_delete(request, id_listado_v):
    try:
        venta = VentaMaquinaria.objects.get(id_listado_v=id_listado_v)
        venta.delete()
        return Response({'message': 'Venta eliminada.'}, status=status.HTTP_200_OK)
    except VentaMaquinaria.DoesNotExist:
        return Response({'error': 'Venta no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def comprar_maquinaria(request, id_listado_v):
    try:
        venta = VentaMaquinaria.objects.get(id_listado_v=id_listado_v)
        comprador = request.headers.get('X-User-Token')
        if comprador == venta.propietario:
            return Response({'error': 'No puede comprar su propia maquinaria.'}, status=status.HTTP_400_BAD_REQUEST)

        # Simula notificación (en el proyecto probado lo mandaba a RabbitMQ)
        print(f'[NOTIFICACION] Usuario {comprador} compró maquinaria {venta.id_maquinaria.id_maquinaria} de {venta.propietario}')

        return Response({'message': 'Compra registrada, notificación enviada.'}, status=status.HTTP_200_OK)
    except VentaMaquinaria.DoesNotExist:
        return Response({'error': 'Venta no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

# Servicio

@csrf_exempt
@api_view(['GET', 'POST'])
def servicio_list_create(request):
    if request.method == 'GET':
        servicio = ReservaMaquinaria.objects.all()
        serializer = ReservaMaquinariaSerializer(servicio, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        next_id = obtener_contador('id_listado_r')
        id_listado_r = f'SER{next_id:05d}'

        data = request.data.copy()
        data['id_listado_r'] = id_listado_r

        # Validación de fechas
        try:
            fecha_inicio = datetime.strptime(data.get('fecha_inicio'), '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(data.get('fecha_fin'), '%Y-%m-%d').date()
            today = datetime.today().date()

            if fecha_inicio < today:
                return Response({'error': 'Fecha de inicio debe ser hoy o futura.'}, status=status.HTTP_400_BAD_REQUEST)
            if fecha_fin < fecha_inicio:
                return Response({'error': 'Fecha de fin no puede ser anterior a la fecha de inicio.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Error en formato de fechas: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReservaMaquinariaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def servicio_delete(request, id_listado_r):
    try:
        servicio = ReservaMaquinaria.objects.get(id_listado_r=id_listado_r)
        servicio.delete()
        return Response({'message': 'Servicio eliminado.'}, status=status.HTTP_200_OK)
    except ReservaMaquinaria.DoesNotExist:
        return Response({'error': 'Servicio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def pedir_servicio(request, id_listado_r):
    try:
        servicio = ReservaMaquinaria.objects.get(id_listado_r=id_listado_r)
        solicitante = request.headers.get('X-User-Token')
        if solicitante == servicio.propietario:
            return Response({'error': 'No puede pedir su propio servicio.'}, status=status.HTTP_400_BAD_REQUEST)

        # Simula notificación (en el proyecto probado lo mandaba a RabbitMQ)
        print(f'[NOTIFICACION] Usuario {solicitante} pidió servicio de maquinaria {servicio.id_maquinaria.id_maquinaria} de {servicio.propietario}')

        return Response({'message': 'Pedido registrado, notificación enviada.'}, status=status.HTTP_200_OK)
    except ReservaMaquinaria.DoesNotExist:
        return Response({'error': 'Servicio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

