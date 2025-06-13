from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notificacion
from .serializers import NotificacionSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def notificaciones_list_create(request):
    user_token = request.headers.get('X-User-Token')
    if request.method == 'GET':
        notificaciones = Notificacion.objects.filter(propietario=user_token)
        serializer = NotificacionSerializer(notificaciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data.copy()
        data['propietario'] = user_token
        serializer = NotificacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def notificacion_delete(request, id):
    try:
        notificacion = Notificacion.objects.get(id=id)
        notificacion.delete()
        return Response({'message': 'Notificación eliminada.'}, status=status.HTTP_200_OK)
    except Notificacion.DoesNotExist:
        return Response({'error': 'Notificación no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

