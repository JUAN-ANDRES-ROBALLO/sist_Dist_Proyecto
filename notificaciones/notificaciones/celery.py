from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer la configuración predeterminada de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones.settings')

app = Celery('notificaciones')

# Lee configuración desde Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-descubre tareas desde cualquier archivo tasks.py en las apps instaladas
app.autodiscover_tasks()
    
