from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def signup(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        cedula = serializer.validated_data.get('cedula')
        email = serializer.validated_data.get('email')
        if Usuario.objects.filter(cedula=cedula).exists():
            return Response({'error': 'Cédula ya registrada.'}, status=status.HTTP_400_BAD_REQUEST)
        if Usuario.objects.filter(email=email).exists():
            return Response({'error': 'Email ya registrado.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'message': 'Usuario creado exitosamente.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        usuario = Usuario.objects.get(email=email, password=password)
        return Response({'message': 'Login exitoso.', 'cedula': usuario.cedula}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)



from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')
