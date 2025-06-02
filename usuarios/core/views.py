from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json
@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if Usuario.objects.filter(cedula=data['cedula']).exists():
            return JsonResponse({'error': 'Cédula ya registrada'}, status=400)
        if Usuario.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Email ya registrado'}, status=400)
        usuario = Usuario.objects.create(**data)
        return JsonResponse({'status': 'Registrado', 'usuario': usuario.nombre})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
def index(request):
    return render(request, "index.html")
