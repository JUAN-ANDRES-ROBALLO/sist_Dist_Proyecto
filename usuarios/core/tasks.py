from celery import Celery

app = Celery('usuarios')
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def publicar_usuario(usuario_data):
    print(f"Publicar usuario a otras apps: {usuario_data}")
