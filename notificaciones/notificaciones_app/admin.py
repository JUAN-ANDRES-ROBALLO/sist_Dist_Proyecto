from django.contrib import admin
from .models import Notificacion

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_cedula', 'mensaje', 'tipo', 'fecha_creacion', 'leida')
    list_filter = ('usuario_cedula', 'tipo', 'leida')
    search_fields = ('usuario_cedula', 'mensaje', 'tipo')
    ordering = ('-fecha_creacion',) 