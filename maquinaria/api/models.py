from django.db import models

class Contador(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nombre}: {self.valor}'

class Maquinaria(models.Model):
    id_maquinaria = models.CharField(primary_key=True, max_length=20)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return f'{self.id_maquinaria} - {self.tipo} {self.marca} {self.modelo}'

class VentaMaquinaria(models.Model):
    id_listado_v = models.CharField(primary_key=True, max_length=20)
    id_maquinaria = models.ForeignKey(Maquinaria, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=20)
    fecha_v = models.DateTimeField(auto_now_add=True)
    precio = models.FloatField()

    def __str__(self):
        return f'Venta {self.id_listado_v} - {self.id_maquinaria}'

class ReservaMaquinaria(models.Model):
    id_listado_r = models.CharField(primary_key=True, max_length=20)
    id_maquinaria = models.ForeignKey(Maquinaria, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=20)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Reserva {self.id_listado_r} - {self.id_maquinaria}'

