from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notificacion
from .serializers import NotificacionSerializer
from .tasks import procesar_notificacion_asincrona
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({"status": "healthy", "service": "notificaciones"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def listar_notificaciones(request):
    """Listar notificaciones de un usuario (por cédula)"""
    cedula = request.query_params.get('cedula')
    if not cedula:
        return Response({'error': 'Debe proporcionar la cédula'}, status=status.HTTP_400_BAD_REQUEST)
    notificaciones = Notificacion.objects.filter(usuario_cedula=cedula).order_by('-fecha_creacion')
    serializer = NotificacionSerializer(notificaciones, many=True)
    return Response({'notificaciones': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def crear_notificacion(request):
    """Crear una nueva notificación"""
    serializer = NotificacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'notificacion': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Datos inválidos', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_notificacion(request, pk):
    """Eliminar una notificación por id"""
    try:
        notificacion = Notificacion.objects.get(pk=pk)
        notificacion.delete()
        return Response({'message': 'Notificación eliminada'}, status=status.HTTP_200_OK)
    except Notificacion.DoesNotExist:
        return Response({'error': 'Notificación no encontrada'}, status=status.HTTP_404_NOT_FOUND) 