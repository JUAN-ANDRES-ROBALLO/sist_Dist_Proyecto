from django.db import models

class Usuario(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    estado = models.CharField(max_length=100)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

