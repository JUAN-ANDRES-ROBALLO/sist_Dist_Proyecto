from rest_framework import serializers
from .models import Finca, Parcela, Cultivo

class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = ['id', 'id_productor', 'nombre_finca', 'ubicacion', 'tipo_de_suelo', 'fecha_registro_finca']

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = ['id_productor_p', 'nombre_finca_p', 'id_parcela', 'superficie']

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ['id', 'id_finca', 'tipo_cultivo', 'area_cultivo', 'fecha_siembra', 'fecha_cosecha', 'estado_cultivo'] 