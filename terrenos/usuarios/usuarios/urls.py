"""usuarios URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
]

