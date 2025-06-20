from django.shortcuts import render
from django.http import JsonResponse
from .models import Notificacion
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def mostrar_notificaciones(request):
    if request.method == 'GET':
        cedula = request.session.get('usuario')
        if not cedula:
            return JsonResponse({'error': 'Usuario no autenticado'}, status=403)
        notifs = Notificacion.objects.filter(usuario_destino=cedula).order_by('-fecha')
        data = [{'id': n.id, 'tipo': n.tipo, 'contenido': n.contenido, 'fecha': n.fecha.strftime('%Y-%m-%d %H:%M')} for n in notifs]
        return JsonResponse({'notificaciones': data})

@csrf_exempt
def eliminar_notificacion(request, notif_id):
    if request.method == 'DELETE':
        try:
            notif = Notificacion.objects.get(id=notif_id)
            notif.delete()
            return JsonResponse({'success': 'Notificación eliminada'})
        except Notificacion.DoesNotExist:
            return JsonResponse({'error': 'No encontrada'}, status=404)

