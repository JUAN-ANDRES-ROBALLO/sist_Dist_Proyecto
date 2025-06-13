from django.urls import path
from . import views

urlpatterns = [
    path('finca/', views.finca_list_create),
    path('finca/<str:id_productor>/<str:nombre_finca>/', views.finca_delete),

    path('parcela/', views.parcela_list_create),
    path('parcela/<str:id_productor_p>/<str:nombre_finca_p>/<str:id_parcela>/', views.parcela_delete),
]

