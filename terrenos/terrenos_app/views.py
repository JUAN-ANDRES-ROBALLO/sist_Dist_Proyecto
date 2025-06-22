from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from .models import Finca, Parcela, Cultivo
from .serializers import FincaSerializer, ParcelaSerializer, CultivoSerializer
from .tasks import notificar_eliminacion_finca, notificar_eliminacion_parcela
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def listar_fincas(request):
    """Listar fincas de un productor específico"""
    id_productor = request.query_params.get('id_productor')
    if not id_productor:
        return Response({'error': 'Debe proporcionar el ID del productor'}, status=status.HTTP_400_BAD_REQUEST)
    
    fincas = Finca.objects.filter(id_productor=id_productor)
    serializer = FincaSerializer(fincas, many=True)
    return Response({'fincas': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def agregar_finca(request):
    """Agregar una nueva finca"""
    try:
        serializer = FincaSerializer(data=request.data)
        if serializer.is_valid():
            # Verificar si ya existe la finca
            if Finca.objects.filter(
                id_productor=serializer.validated_data['id_productor'],
                nombre_finca=serializer.validated_data['nombre_finca']
            ).exists():
                return Response({
                    'error': 'Ya existe una finca con ese nombre para este productor'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'finca': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        return Response({
            'error': 'Ya existe una finca con ese nombre para este productor'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_finca(request):
    """Eliminar una finca y sus parcelas asociadas"""
    id_productor = request.data.get('id_productor')
    nombre_finca = request.data.get('nombre_finca')
    
    if not id_productor or not nombre_finca:
        return Response({
            'error': 'Debe proporcionar id_productor y nombre_finca'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        finca = Finca.objects.get(id_productor=id_productor, nombre_finca=nombre_finca)
        
        # Eliminar parcelas asociadas primero
        Parcela.objects.filter(
            id_productor_p=id_productor,
            nombre_finca_p=nombre_finca
        ).delete()
        
        # Eliminar la finca
        finca.delete()
        
        # Publicar evento en Celery para notificaciones
        notificar_eliminacion_finca.delay(id_productor, nombre_finca)
        
        return Response({'message': 'Finca eliminada exitosamente'}, status=status.HTTP_200_OK)
    except Finca.DoesNotExist:
        return Response({'error': 'Finca no encontrada'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def listar_parcelas(request):
    """Listar parcelas de una finca específica"""
    id_productor = request.query_params.get('id_productor')
    nombre_finca = request.query_params.get('nombre_finca')
    
    if not id_productor or not nombre_finca:
        return Response({
            'error': 'Debe proporcionar id_productor y nombre_finca'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    parcelas = Parcela.objects.filter(
        id_productor_p=id_productor,
        nombre_finca_p=nombre_finca
    )
    serializer = ParcelaSerializer(parcelas, many=True)
    return Response({'parcelas': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def agregar_parcela(request):
    """Agregar una nueva parcela"""
    try:
        serializer = ParcelaSerializer(data=request.data)
        if serializer.is_valid():
            # Verificar si ya existe la parcela
            if Parcela.objects.filter(
                id_productor_p=serializer.validated_data['id_productor_p'],
                nombre_finca_p=serializer.validated_data['nombre_finca_p'],
                id_parcela=serializer.validated_data['id_parcela']
            ).exists():
                return Response({
                    'error': 'Ya existe una parcela con ese ID en esta finca'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Verificar que la finca existe
            if not Finca.objects.filter(
                id_productor=serializer.validated_data['id_productor_p'],
                nombre_finca=serializer.validated_data['nombre_finca_p']
            ).exists():
                return Response({
                    'error': 'La finca especificada no existe'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'parcela': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        return Response({
            'error': 'Ya existe una parcela con ese ID en esta finca'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_parcela(request):
    """Eliminar una parcela específica"""
    id_productor = request.data.get('id_productor_p')
    nombre_finca = request.data.get('nombre_finca_p')
    id_parcela = request.data.get('id_parcela')
    
    if not id_productor or not nombre_finca or not id_parcela:
        return Response({
            'error': 'Debe proporcionar id_productor_p, nombre_finca_p e id_parcela'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        parcela = Parcela.objects.get(
            id_productor_p=id_productor,
            nombre_finca_p=nombre_finca,
            id_parcela=id_parcela
        )
        parcela.delete()
        
        # Publicar evento en Celery para notificaciones
        notificar_eliminacion_parcela.delay(id_productor, nombre_finca, id_parcela)
        
        return Response({'message': 'Parcela eliminada exitosamente'}, status=status.HTTP_200_OK)
    except Parcela.DoesNotExist:
        return Response({'error': 'Parcela no encontrada'}, status=status.HTTP_404_NOT_FOUND)

# Vistas para Cultivos
@api_view(['GET'])
def listar_cultivos(request):
    """Listar cultivos de una finca específica"""
    id_productor = request.query_params.get('id_productor')
    nombre_finca = request.query_params.get('nombre_finca')
    
    if not id_productor or not nombre_finca:
        return Response({
            'error': 'Debe proporcionar id_productor y nombre_finca'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Obtener la finca
        finca = Finca.objects.get(id_productor=id_productor, nombre_finca=nombre_finca)
        
        # Obtener cultivos de esa finca
        cultivos = Cultivo.objects.filter(id_finca=finca)
        serializer = CultivoSerializer(cultivos, many=True)
        return Response({'cultivos': serializer.data}, status=status.HTTP_200_OK)
    except Finca.DoesNotExist:
        return Response({'error': 'Finca no encontrada'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def agregar_cultivo(request):
    """Agregar un nuevo cultivo"""
    try:
        serializer = CultivoSerializer(data=request.data)
        if serializer.is_valid():
            # Verificar que la finca existe
            try:
                finca = Finca.objects.get(id=serializer.validated_data['id_finca'].id)
            except Finca.DoesNotExist:
                return Response({
                    'error': 'La finca especificada no existe'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'cultivo': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        return Response({
            'error': 'Error al crear el cultivo'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({"status": "healthy", "service": "terrenos"}, status=status.HTTP_200_OK) 