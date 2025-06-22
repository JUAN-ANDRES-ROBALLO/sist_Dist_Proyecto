from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.db import IntegrityError
import logging
from .models import Usuario
from .serializers import (
    UsuarioSignupSerializer, 
    UsuarioLoginSerializer, 
    UsuarioResponseSerializer
)
from .tasks import notificar_registro_usuario, enviar_notificacion_usuario
from django.shortcuts import render

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """
    Endpoint para registro de usuarios
    """
    try:
        serializer = UsuarioSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Enviar notificación asíncrona de bienvenida
            notificar_registro_usuario.delay(user.cedula, user.nombre)
            
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user': UsuarioResponseSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError as e:
        logger.error(f"IntegrityError en signup: {str(e)}")
        if 'usuarios_cedula_key' in str(e):
            return Response({
                'error': 'Ya existe un usuario con esa cédula'
            }, status=status.HTTP_400_BAD_REQUEST)
        elif 'usuarios_email_key' in str(e):
            return Response({
                'error': 'Ya existe un usuario con ese email'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'error': 'Error al crear el usuario'
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error en signup: {str(e)}", exc_info=True)
        return Response({
            'error': 'Error interno del servidor',
            'debug_info': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Endpoint para login de usuarios
    """
    try:
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Buscar usuario por email
            try:
                user = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                return Response({
                    'error': 'Credenciales inválidas'
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            # Autenticar usuario
            if user.check_password(password):
                if not user.activo:
                    return Response({
                        'error': 'Usuario inactivo'
                    }, status=status.HTTP_401_UNAUTHORIZED)
                
                # Actualizar último acceso
                user.save()  # Esto actualiza fecha_ultimo_acceso
                
                return Response({
                    'message': 'Login exitoso',
                    'user': UsuarioResponseSerializer(user).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Credenciales inválidas'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'error': 'Datos inválidos',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'error': 'Error interno del servidor'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_user_info(request, cedula):
    """
    Endpoint para obtener información de un usuario por cédula
    """
    try:
        user = Usuario.objects.get(cedula=cedula)
        return Response({
            'user': UsuarioResponseSerializer(user).data
        }, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({
            'error': 'Usuario no encontrado'
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'error': 'Error interno del servidor'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_users(request):
    """
    Endpoint para listar usuarios (solo usuarios activos)
    """
    try:
        users = Usuario.objects.filter(activo=True)
        serializer = UsuarioResponseSerializer(users, many=True)
        return Response({
            'users': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error': 'Error interno del servidor'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({"status": "healthy", "service": "usuarios"}, status=status.HTTP_200_OK) 