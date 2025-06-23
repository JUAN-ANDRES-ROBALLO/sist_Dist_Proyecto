from django.urls import path
from . import views

urlpatterns = [
    # Maquinaria
    path('api/maquinaria/health/', views.health_check, name='health_check'),
    path('api/maquinaria/maquinaria/', views.listar_maquinaria_propia, name='listar_maquinaria_propia'),
    path('api/maquinaria/maquinaria/crear/', views.crear_maquinaria, name='crear_maquinaria'),
    path('api/maquinaria/agregar/', views.crear_maquinaria, name='agregar_maquinaria'),  # Endpoint alternativo para frontend
    path('api/maquinaria/maquinaria/<str:id_maquinaria>/eliminar/', views.eliminar_maquinaria, name='eliminar_maquinaria'),
    
    # Ventas
    path('api/maquinaria/ventas/', views.listar_ventas, name='listar_ventas'),
    path('api/maquinaria/ventas/crear/', views.crear_venta, name='crear_venta'),
    
    # Reservas
    path('api/maquinaria/reservas/', views.listar_reservas, name='listar_reservas'),
    path('api/maquinaria/reservas/crear/', views.crear_reserva, name='crear_reserva'),
] 