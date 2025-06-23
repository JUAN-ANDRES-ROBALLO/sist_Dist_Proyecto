from django.urls import path
from . import views

urlpatterns = [
    path('api/notificaciones/health/', views.health_check, name='health_check'),
    path('api/notificaciones/notificaciones/', views.listar_notificaciones, name='listar_notificaciones'),
    path('api/notificaciones/notificaciones/crear/', views.crear_notificacion, name='crear_notificacion'),
    path('api/notificaciones/agregar/', views.crear_notificacion, name='agregar_notificacion'),
    path('api/notificaciones/notificaciones/<int:pk>/eliminar/', views.eliminar_notificacion, name='eliminar_notificacion'),
] 