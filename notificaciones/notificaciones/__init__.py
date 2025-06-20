from __future__ import absolute_import, unicode_literals

# Esto permite que Django cargue Celery al iniciar el proyecto
from .celery import app as celery_app

__all__ = ('celery_app',)

