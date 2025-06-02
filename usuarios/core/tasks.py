from celery import Celery
app = Celery('usuarios')
app.config_from_object('django.conf:settings', namespace='CELERY')
@app.task
def enviar_notificacion(cedula):
    print(f"Enviar notificación a {cedula}")
