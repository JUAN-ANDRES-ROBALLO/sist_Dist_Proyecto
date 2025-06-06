from django.urls import path
from .views import registrar_usuario, index, obtener_usuario

urlpatterns = [
    path('', index),
    path('registro/', registrar_usuario),
    path('usuario/<cedula>/', obtener_usuario),
]
