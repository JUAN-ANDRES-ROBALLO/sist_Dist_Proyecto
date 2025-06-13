from django.db import models

class Usuario(models.Model):
    cedula = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=20)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} ({self.cedula})'

