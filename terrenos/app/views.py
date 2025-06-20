from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Finca, Parcela
from .tasks import enviar_evento_eliminacion
import json

@csrf_exempt
def agregar_finca(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if Finca.objects.filter(id_productor=data['id_productor'], nombre_finca=data['nombre_finca']).exists():
            return JsonResponse({'error': 'Finca ya registrada'}, status=400)
        Finca.objects.create(**data)
        return JsonResponse({'success': 'Finca agregada correctamente'})

@csrf_exempt
def agregar_parcela(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if Parcela.objects.filter(finca_nombre_p=data['finca_nombre_p'], id_parcela=data['id_parcela']).exists():
            return JsonResponse({'error': 'Parcela ya registrada'}, status=400)
        Parcela.objects.create(**data)
        return JsonResponse({'success': 'Parcela agregada correctamente'})

@csrf_exempt
def eliminar_finca(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            finca = Finca.objects.get(id_productor=data['id_productor'], nombre_finca=data['nombre_finca'])
            finca.delete()
            enviar_evento_eliminacion.delay("eliminacion", "finca", data['nombre_finca'], data['id_productor'])
            return JsonResponse({'success': 'Finca eliminada'})
        except Finca.DoesNotExist:
            return JsonResponse({'error': 'Finca no encontrada'}, status=404)

@csrf_exempt
def eliminar_parcela(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            parcela = Parcela.objects.get(finca_nombre_p=data['finca_nombre_p'], id_parcela=data['id_parcela'])
            parcela.delete()
            enviar_evento_eliminacion.delay("eliminacion", "parcela", data['id_parcela'], data.get('usuario', ''))
            return JsonResponse({'success': 'Parcela eliminada'})
        except Parcela.DoesNotExist:
            return JsonResponse({'error': 'Parcela no encontrada'}, status=404)

