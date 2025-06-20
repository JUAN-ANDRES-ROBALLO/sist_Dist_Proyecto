# maquinaria/maquinaria/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece el módulo de configuración predeterminado de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maquinaria.settings')

app = Celery('maquinaria')

# Lee la configuración desde el archivo de Django y usa el namespace CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre tareas automáticamente en todas las apps de Django registradas
app.autodiscover_tasks()

