from rest_framework import serializers
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria

class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquinaria
        fields = ['id_maquinaria', 'propietario_m', 'tipo', 'marca', 'modelo', 'año']

class VentaMaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaMaquinaria
        fields = ['id_listado_v', 'id_maquinaria', 'propietario_v', 'fecha_v', 'precio']

class ReservaMaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaMaquinaria
        fields = ['id_listado_r', 'id_maquinaria', 'propietario_r', 'fecha_inicio', 'fecha_fin'] 