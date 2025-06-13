from rest_framework import serializers
from .models import Finca, Parcela

class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = '__all__'

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = '__all__'

