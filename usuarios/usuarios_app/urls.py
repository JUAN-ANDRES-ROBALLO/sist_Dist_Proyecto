from django.urls import path
from . import views

urlpatterns = [
    path('api/usuarios/health/', views.health_check, name='health_check'),
    path('api/usuarios/signup/', views.signup, name='signup'),
    path('api/usuarios/login/', views.login, name='login'),
    path('api/usuarios/', views.list_users, name='list_users'),
    path('api/usuarios/<str:cedula>/', views.get_user_info, name='get_user_info'),
] 