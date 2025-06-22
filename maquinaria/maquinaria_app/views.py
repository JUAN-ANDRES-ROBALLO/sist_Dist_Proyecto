from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria
from .serializers import MaquinariaSerializer, VentaMaquinariaSerializer, ReservaMaquinariaSerializer
from .tasks import notificar_venta_maquinaria, notificar_reserva_maquinaria
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def listar_maquinaria_propia(request):
    """Listar maquinaria de un propietario específico"""
    propietario = request.query_params.get('propietario')
    if not propietario:
        return Response({'error': 'Debe proporcionar el propietario'}, status=status.HTTP_400_BAD_REQUEST)
    
    maquinaria = Maquinaria.objects.filter(propietario_m=propietario)
    serializer = MaquinariaSerializer(maquinaria, many=True)
    return Response({'maquinaria': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def crear_maquinaria(request):
    """Crear nueva maquinaria"""
    serializer = MaquinariaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'maquinaria': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Datos inválidos', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_maquinaria(request, id_maquinaria):
    """Eliminar maquinaria por ID"""
    try:
        maquinaria = Maquinaria.objects.get(id_maquinaria=id_maquinaria)
        maquinaria.delete()
        return Response({'message': 'Maquinaria eliminada'}, status=status.HTTP_200_OK)
    except Maquinaria.DoesNotExist:
        return Response({'error': 'Maquinaria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def listar_ventas(request):
    """Listar todas las ventas de maquinaria"""
    ventas = VentaMaquinaria.objects.all()
    serializer = VentaMaquinariaSerializer(ventas, many=True)
    return Response({'ventas': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def crear_venta(request):
    """Crear nueva venta de maquinaria"""
    serializer = VentaMaquinariaSerializer(data=request.data)
    if serializer.is_valid():
        venta = serializer.save()
        
        # Enviar notificación asíncrona
        notificar_venta_maquinaria.delay(
            venta.propietario_v,
            venta.id_maquinaria,
            venta.precio
        )
        
        return Response({'venta': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Datos inválidos', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_reservas(request):
    """Listar todas las reservas de maquinaria"""
    reservas = ReservaMaquinaria.objects.all()
    serializer = ReservaMaquinariaSerializer(reservas, many=True)
    return Response({'reservas': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def crear_reserva(request):
    """Crear nueva reserva de maquinaria"""
    serializer = ReservaMaquinariaSerializer(data=request.data)
    if serializer.is_valid():
        reserva = serializer.save()
        
        # Enviar notificación asíncrona
        notificar_reserva_maquinaria.delay(
            reserva.propietario_r,
            reserva.id_maquinaria,
            reserva.fecha_inicio,
            reserva.fecha_fin
        )
        
        return Response({'reserva': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Datos inválidos', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({"status": "healthy", "service": "maquinaria"}, status=status.HTTP_200_OK) 