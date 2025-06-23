from django.urls import path
from . import views

urlpatterns = [
    path('api/terrenos/health/', views.health_check, name='health_check'),
    # Fincas
    path('api/terrenos/fincas/', views.listar_fincas, name='listar_fincas'),
    path('api/terrenos/fincas/agregar/', views.agregar_finca, name='agregar_finca'),
    path('api/terrenos/fincas/eliminar/', views.eliminar_finca, name='eliminar_finca'),
    
    # Parcelas
    path('api/terrenos/parcelas/', views.listar_parcelas, name='listar_parcelas'),
    path('api/terrenos/parcelas/agregar/', views.agregar_parcela, name='agregar_parcela'),
    path('api/terrenos/parcelas/eliminar/', views.eliminar_parcela, name='eliminar_parcela'),
    
    # Cultivos
    path('api/terrenos/cultivos/', views.listar_cultivos, name='listar_cultivos'),
    path('api/terrenos/cultivos/agregar/', views.agregar_cultivo, name='agregar_cultivo'),
] 