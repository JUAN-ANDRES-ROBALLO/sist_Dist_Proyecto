from django.db import models

class Notificacion(models.Model):
    """
    Modelo para notificaciones persistentes.
    """
    id = models.AutoField(primary_key=True)
    usuario_cedula = models.CharField(max_length=10, help_text="Cédula del usuario receptor")
    mensaje = models.TextField(help_text="Mensaje de la notificación")
    tipo = models.CharField(max_length=50, help_text="Tipo de notificación")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)

    class Meta:
        db_table = 'notificaciones'
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Notificación para {self.usuario_cedula}: {self.mensaje[:30]}..." 