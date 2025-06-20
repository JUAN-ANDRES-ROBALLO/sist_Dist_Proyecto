from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if Usuario.objects.filter(cedula=data['cedula']).exists():
            return JsonResponse({'error': 'Cédula ya registrada'}, status=400)
        if Usuario.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Email ya registrado'}, status=400)
        Usuario.objects.create(
            cedula=data['cedula'],
            nombre=data['nombre'],
            email=data['email'],
            contraseña=make_password(data['contraseña']),
            estado=data['estado']
        )
        return JsonResponse({'success': 'Usuario creado'})
    return render(request, 'usuarios/signup.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = Usuario.objects.get(email=data['email'])
            if check_password(data['contraseña'], user.contraseña):
                request.session['usuario'] = user.cedula
                return JsonResponse({'success': 'Login correcto'})
            else:
                return JsonResponse({'error': 'Contraseña incorrecta'}, status=401)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    return render(request, 'usuarios/login.html')

def homepage(request):
    if 'usuario' not in request.session:
        return redirect('/usuarios/login/')
    return render(request, 'usuarios/homepage.html')

def inicio(request):
    return render(request, 'usuarios/inicio.html')

