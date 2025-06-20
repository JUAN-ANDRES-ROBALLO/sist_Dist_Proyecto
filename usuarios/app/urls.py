from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('homepage/', views.homepage),
]

