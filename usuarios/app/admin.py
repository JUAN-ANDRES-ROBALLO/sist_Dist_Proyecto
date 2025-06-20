from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'email', 'estado', 'fecha_de_registro')
    search_fields = ('cedula', 'nombre', 'email')

