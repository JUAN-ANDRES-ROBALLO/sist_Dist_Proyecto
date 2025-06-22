from django.urls import path
from . import views

urlpatterns = [
    # Maquinaria
    path('health/', views.health_check, name='health_check'),
    path('maquinaria/', views.listar_maquinaria_propia, name='listar_maquinaria_propia'),
    path('maquinaria/crear/', views.crear_maquinaria, name='crear_maquinaria'),
    path('agregar/', views.crear_maquinaria, name='agregar_maquinaria'),  # Endpoint alternativo para frontend
    path('maquinaria/<str:id_maquinaria>/eliminar/', views.eliminar_maquinaria, name='eliminar_maquinaria'),
    
    # Ventas
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    
    # Reservas
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
] 