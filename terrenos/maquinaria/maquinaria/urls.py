"""maquinaria URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

    path('mi_maquinaria/', TemplateView.as_view(template_name='mi_maquinaria.html'), name='mi_maquinaria'),
    path('servicio/', TemplateView.as_view(template_name='servicio.html'), name='servicio'),
    path('venta/', TemplateView.as_view(template_name='venta.html'), name='venta'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
]

