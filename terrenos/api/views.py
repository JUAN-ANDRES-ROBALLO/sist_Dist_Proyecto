from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Finca, Parcela
from .serializers import FincaSerializer, ParcelaSerializer
from django.views.decorators.csrf import csrf_exempt

# Finca

@csrf_exempt
@api_view(['GET', 'POST'])
def finca_list_create(request):
    if request.method == 'GET':
        id_productor = request.headers.get('X-User-Token')
        fincas = Finca.objects.filter(id_productor=id_productor)
        serializer = FincaSerializer(fincas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FincaSerializer(data=request.data)
        if serializer.is_valid():
            if Finca.objects.filter(
                id_productor=serializer.validated_data['id_productor'],
                nombre_finca=serializer.validated_data['nombre_finca']
            ).exists():
                return Response({'error': 'Finca ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def finca_delete(request, id_productor, nombre_finca):
    try:
        finca = Finca.objects.get(id_productor=id_productor, nombre_finca=nombre_finca)
        finca.delete()
        return Response({'message': 'Finca eliminada.'}, status=status.HTTP_200_OK)
    except Finca.DoesNotExist:
        return Response({'error': 'Finca no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

# Parcela

@csrf_exempt
@api_view(['GET', 'POST'])
def parcela_list_create(request):
    if request.method == 'GET':
        id_productor_p = request.headers.get('X-User-Token')
        parcelas = Parcela.objects.filter(id_productor_p=id_productor_p)
        serializer = ParcelaSerializer(parcelas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ParcelaSerializer(data=request.data)
        if serializer.is_valid():
            if Parcela.objects.filter(
                id_productor_p=serializer.validated_data['id_productor_p'],
                nombre_finca_p=serializer.validated_data['nombre_finca_p'],
                id_parcela=serializer.validated_data['id_parcela']
            ).exists():
                return Response({'error': 'Parcela ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def parcela_delete(request, id_productor_p, nombre_finca_p, id_parcela):
    try:
        parcela = Parcela.objects.get(
            id_productor_p=id_productor_p,
            nombre_finca_p=nombre_finca_p,
            id_parcela=id_parcela
        )
        parcela.delete()
        return Response({'message': 'Parcela eliminada.'}, status=status.HTTP_200_OK)
    except Parcela.DoesNotExist:
        return Response({'error': 'Parcela no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

