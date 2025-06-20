from django.urls import path
from . import views

urlpatterns = [
    path('', views.maquinaria_home, name='maquinaria_home'),
    path('form/agregar/', views.form_agregar_maquinaria, name='form_agregar_maquinaria'),
    path('api/maquinaria/agregar/', views.agregar_maquinaria),
    path('api/maquinaria/eliminar/', views.eliminar_maquinaria),
    path('api/maquinaria/listar/', views.listar_mi_maquinaria),
    path('api/maquinaria/venta/agregar/', views.poner_en_venta),
    path('api/maquinaria/venta/quitar/', views.sacar_de_venta),
    path('api/maquinaria/venta/listar/', views.maquinaria_en_venta),
    path('api/maquinaria/venta/comprar/', views.comprar_maquinaria),
    path('api/maquinaria/servicio/agregar/', views.poner_en_servicio),
    path('api/maquinaria/servicio/quitar/', views.sacar_de_servicio),
    path('api/maquinaria/servicio/listar/', views.maquinaria_en_servicio),
    path('api/maquinaria/servicio/pedir/', views.pedir_maquinaria),
]

