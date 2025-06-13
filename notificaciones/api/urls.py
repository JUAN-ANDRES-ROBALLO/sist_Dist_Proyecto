from django.urls import path
from . import views

urlpatterns = [
    path('notificaciones/', views.notificaciones_list_create),
    path('notificaciones/<int:id>/', views.notificacion_delete),
]

