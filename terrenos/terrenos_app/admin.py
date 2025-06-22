from django.contrib import admin
from .models import Finca, Parcela

@admin.register(Finca)
class FincaAdmin(admin.ModelAdmin):
    list_display = ('id_productor', 'nombre_finca', 'ubicacion', 'tipo_de_suelo', 'fecha_registro_finca')
    list_filter = ('id_productor', 'tipo_de_suelo', 'fecha_registro_finca')
    search_fields = ('id_productor', 'nombre_finca', 'ubicacion')
    ordering = ('id_productor', 'nombre_finca')

@admin.register(Parcela)
class ParcelaAdmin(admin.ModelAdmin):
    list_display = ('id_productor_p', 'nombre_finca_p', 'id_parcela', 'superficie')
    list_filter = ('id_productor_p', 'nombre_finca_p')
    search_fields = ('id_productor_p', 'nombre_finca_p', 'id_parcela')
    ordering = ('id_productor_p', 'nombre_finca_p', 'id_parcela') 