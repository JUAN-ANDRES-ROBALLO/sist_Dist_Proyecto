from django.db import models

class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('compra', 'Compra'),
        ('servicio', 'Servicio'),
        ('eliminacion', 'Eliminación'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    contenido = models.TextField()
    usuario_destino = models.CharField(max_length=50)  # cedula
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} → {self.usuario_destino}: {self.contenido[:30]}"

