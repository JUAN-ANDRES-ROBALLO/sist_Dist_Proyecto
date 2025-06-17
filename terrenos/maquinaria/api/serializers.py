from rest_framework import serializers
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria, Contador

class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquinaria
        fields = '__all__'

class VentaMaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaMaquinaria
        fields = '__all__'

class ReservaMaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaMaquinaria
        fields = '__all__'

class ContadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contador
        fields = '__all__'

