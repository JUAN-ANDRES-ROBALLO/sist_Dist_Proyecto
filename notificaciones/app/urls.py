from django.urls import path
from .views import mostrar_notificaciones, eliminar_notificacion

urlpatterns = [
    path('', mostrar_notificaciones, name='mostrar_notificaciones'),
    path('eliminar/<int:notif_id>/', eliminar_notificacion, name='eliminar_notificacion'),
]

