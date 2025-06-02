from django.urls import path
from .views import registrar_usuario, index
urlpatterns = [
    path('registro/', registrar_usuario),
    path('', index)
]
