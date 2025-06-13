from django.db import models

class Finca(models.Model):
    id_productor = models.CharField(max_length=20)
    nombre_finca = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tipo_de_suelo = models.CharField(max_length=100)
    fecha_registro_finca = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_productor', 'nombre_finca')

    def __str__(self):
        return f'{self.nombre_finca} ({self.id_productor})'

class Parcela(models.Model):
    id_productor_p = models.CharField(max_length=20)
    nombre_finca_p = models.CharField(max_length=100)
    id_parcela = models.CharField(max_length=50)
    superficie = models.FloatField()

    class Meta:
        unique_together = ('id_productor_p', 'nombre_finca_p', 'id_parcela')

    def __str__(self):
        return f'{self.id_parcela} ({self.nombre_finca_p}, {self.id_productor_p})'

