from django.db import models

class Finca(models.Model):
    id_productor = models.CharField(max_length=20)
    nombre_finca = models.CharField(max_length=100)
    ubicación = models.CharField(max_length=200)
    tipo_de_suelo = models.CharField(max_length=100)
    fecha_registro_finca = models.DateField()

    class Meta:
        unique_together = ('id_productor', 'nombre_finca')

class Parcela(models.Model):
    finca_nombre_p = models.CharField(max_length=100)
    id_parcela = models.CharField(max_length=50)
    superficie = models.FloatField()

    class Meta:
        unique_together = ('finca_nombre_p', 'id_parcela')

