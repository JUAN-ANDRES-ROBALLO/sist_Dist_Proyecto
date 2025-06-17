from django.db import models

class Notificacion(models.Model):
    propietario = models.CharField(max_length=20)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notificacion para {self.propietario} - {self.descripcion}'

