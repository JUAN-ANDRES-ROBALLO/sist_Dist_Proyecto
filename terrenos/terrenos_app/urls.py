from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    # Fincas
    path('fincas/', views.listar_fincas, name='listar_fincas'),
    path('fincas/agregar/', views.agregar_finca, name='agregar_finca'),
    path('fincas/eliminar/', views.eliminar_finca, name='eliminar_finca'),
    
    # Parcelas
    path('parcelas/', views.listar_parcelas, name='listar_parcelas'),
    path('parcelas/agregar/', views.agregar_parcela, name='agregar_parcela'),
    path('parcelas/eliminar/', views.eliminar_parcela, name='eliminar_parcela'),
    
    # Cultivos
    path('cultivos/', views.listar_cultivos, name='listar_cultivos'),
    path('cultivos/agregar/', views.agregar_cultivo, name='agregar_cultivo'),
] 