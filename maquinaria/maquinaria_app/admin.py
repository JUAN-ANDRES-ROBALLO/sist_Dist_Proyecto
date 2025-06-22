from django.contrib import admin
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria

@admin.register(Maquinaria)
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id_maquinaria', 'propietario_m', 'tipo', 'marca', 'modelo', 'año')
    list_filter = ('propietario_m', 'tipo', 'marca', 'año')
    search_fields = ('id_maquinaria', 'propietario_m', 'marca', 'modelo')
    ordering = ('propietario_m', 'tipo')

@admin.register(VentaMaquinaria)
class VentaMaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id_listado_v', 'id_maquinaria', 'propietario_v', 'fecha_v', 'precio')
    list_filter = ('propietario_v', 'fecha_v')
    search_fields = ('id_listado_v', 'id_maquinaria', 'propietario_v')
    ordering = ('-fecha_v',)

@admin.register(ReservaMaquinaria)
class ReservaMaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id_listado_r', 'id_maquinaria', 'propietario_r', 'fecha_inicio', 'fecha_fin')
    list_filter = ('propietario_r', 'fecha_inicio', 'fecha_fin')
    search_fields = ('id_listado_r', 'id_maquinaria', 'propietario_r')
 