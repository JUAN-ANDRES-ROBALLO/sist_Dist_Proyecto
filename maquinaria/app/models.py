from django.db import models
from django.conf import settings

class Maquinaria(models.Model):
    id_maquinaria = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    propietario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)

class VentaMaquinaria(models.Model):
    id_listado_v = models.AutoField(primary_key=True)
    maquinaria = models.ForeignKey(Maquinaria, on_delete=models.CASCADE)
    propietario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='ventas_maquinaria')
    fecha_v = models.DateField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class ReservaMaquinaria(models.Model):
    id_listado_r = models.AutoField(primary_key=True)
    maquinaria = models.ForeignKey(Maquinaria, on_delete=models.CASCADE)
    propietario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='reservas_maquinaria')
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

