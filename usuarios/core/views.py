from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

def index(request):
    return render(request, "index.html")

@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cedula = data['cedula']
            nombre = data['nombre']
            email = data['email']

            if Usuario.objects.filter(cedula=cedula).exists():
                return JsonResponse({'error': 'Cédula ya registrada'}, status=400)
            if Usuario.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email ya registrado'}, status=400)

            Usuario.objects.create(cedula=cedula, nombre=nombre, email=email)
            return JsonResponse({'status': 'Usuario registrado correctamente'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def obtener_usuario(request, cedula):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(cedula=cedula)
            data = {
                'cedula': usuario.cedula,
                'nombre': usuario.nombre,
                'email': usuario.email
            }
            return JsonResponse({'usuario': data})
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
