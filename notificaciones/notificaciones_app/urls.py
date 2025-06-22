from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('notificaciones/', views.listar_notificaciones, name='listar_notificaciones'),
    path('notificaciones/crear/', views.crear_notificacion, name='crear_notificacion'),
    path('agregar/', views.crear_notificacion, name='agregar_notificacion'),
    path('notificaciones/<int:pk>/eliminar/', views.eliminar_notificacion, name='eliminar_notificacion'),
] 