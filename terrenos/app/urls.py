from django.urls import path
from . import views

urlpatterns = [
    path('finca/agregar/', views.agregar_finca, name='agregar_finca'),
    path('parcela/agregar/', views.agregar_parcela, name='agregar_parcela'),
    path('finca/eliminar/', views.eliminar_finca, name='eliminar_finca'),
    path('parcela/eliminar/', views.eliminar_parcela, name='eliminar_parcela'),
]

