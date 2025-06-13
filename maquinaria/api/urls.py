from django.urls import path
from . import views

urlpatterns = [
    path('maquinaria/', views.maquinaria_list_create),
    path('maquinaria/<str:id_maquinaria>/', views.maquinaria_delete),

    path('venta/', views.venta_list_create),
    path('venta/<str:id_listado_v>/', views.venta_delete),
    path('comprar/<str:id_listado_v>/', views.comprar_maquinaria),

    path('servicio/', views.servicio_list_create),
    path('servicio/<str:id_listado_r>/', views.servicio_delete),
    path('pedir_servicio/<str:id_listado_r>/', views.pedir_servicio),
]

