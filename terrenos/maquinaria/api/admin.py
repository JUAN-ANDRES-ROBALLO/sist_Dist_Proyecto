from django.contrib import admin
from .models import Maquinaria, VentaMaquinaria, ReservaMaquinaria, Contador

admin.site.register(Maquinaria)
admin.site.register(VentaMaquinaria)
admin.site.register(ReservaMaquinaria)
admin.site.register(Contador)

