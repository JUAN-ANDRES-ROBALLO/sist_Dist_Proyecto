# Sistema de Gestión Agrícola - Arquitectura SOA

Un sistema completo de gestión agrícola construido con arquitectura de servicios orientada (SOA), utilizando microservicios Django, comunicación asíncrona con RabbitMQ/Celery, y frontend moderno.

## Arquitectura del Sistema

### Microservicios
- **usuarios** (Puerto 8001): Gestión de usuarios, autenticación y homepage
- **terrenos** (Puerto 8002): Gestión de fincas y parcelas
- **maquinaria** (Puerto 8003): Gestión de maquinaria, ventas y reservas
- **notificaciones** (Puerto 8004): Sistema de notificaciones persistentes

### Infraestructura
- **PostgreSQL**: Base de datos principal con bases de datos separadas por microservicio
- **RabbitMQ**: Message broker para comunicación asíncrona
- **Nginx**: Reverse proxy y servidor de archivos estáticos
- **Celery**: Workers para procesamiento asíncrono

## Instalación y Uso

### Prerrequisitos
- **Docker** instalado y funcionando
- **Docker Compose** disponible
- Puerto 80 disponible para Nginx
- Puertos 8001-8004 disponibles para los microservicios
- Puertos 5432 (PostgreSQL) y 5672/15672 (RabbitMQ) disponibles

### Paso 1: Verificar Docker
```bash
# Verificar que Docker esté instalado
docker --version
docker compose version

# Si no tienes Docker instalado, instálalo según tu sistema operativo
# Ubuntu/Debian:
# sudo apt update && sudo apt install docker.io docker-compose

# macOS:
# brew install docker docker-compose

# Windows:
# Descargar Docker Desktop desde https://www.docker.com/products/docker-desktop
```

### Paso 2: Clonar/Descargar el Proyecto
```bash
# Navegar al directorio donde quieres el proyecto
cd /ruta/destino

# Si tienes git:
# git clone <url-del-repositorio>

# O descargar y extraer el archivo ZIP
```

### Paso 3: Navegar al Directorio del Proyecto
```bash
cd bbb  # o el nombre de tu carpeta del proyecto
```

### Paso 4: Verificar Estructura del Proyecto
```bash
# Verificar que todos los archivos estén presentes
ls -la

# Deberías ver:
# - docker-compose.yml
# - docker-compose-simple.yml
# - start.sh
# - start-fast.sh
# - init-db.sql
# - frontend/
# - usuarios/
# - terrenos/
# - maquinaria/
# - notificaciones/
# - nginx/
```

### Paso 5: Dar Permisos de Ejecución a los Scripts
```bash
chmod +x start.sh
chmod +x start-fast.sh
```

### Paso 6: Verificar Puertos Disponibles
```bash
# Verificar que los puertos necesarios estén libres
netstat -tuln | grep -E ':(80|8001|8002|8003|8004|5432|5672|15672)'

# Si algún puerto está en uso, detén el servicio que lo use o cambia la configuración
```

### Paso 7: Iniciar el Sistema

#### Opción A: Inicio Completo (Recomendado)
```bash
# Usar el script principal
./start.sh

# O manualmente:
docker compose up --build -d
```

#### Opción B: Inicio Rápido
```bash
# Usar el script de inicio rápido
./start-fast.sh

# O manualmente:
docker compose -f docker-compose-simple.yml up --build -d
```

### Paso 8: Esperar a que los Servicios Estén Listos
```bash
# El sistema tarda aproximadamente 2-3 minutos en estar completamente listo
# Puedes monitorear el progreso con:
docker compose ps

# O ver los logs en tiempo real:
docker compose logs -f
```

### Paso 9: Verificar que Todos los Servicios Estén Funcionando
```bash
# Verificar estado de contenedores
docker compose ps

# Todos los servicios deben mostrar "Up" en la columna Status

# Verificar logs de cada servicio
docker compose logs usuarios
docker compose logs terrenos
docker compose logs maquinaria
docker compose logs notificaciones
docker compose logs nginx
docker compose logs postgres
docker compose logs rabbitmq
```

### Paso 10: Acceder al Sistema
- **Frontend Principal**: http://localhost
- **RabbitMQ Management**: http://localhost:15672
  - Usuario: `farm_user`
  - Contraseña: `farm_password`

## Funcionalidades del Sistema

### Autenticación (App Usuarios)
- **Registro**: Crear nueva cuenta con cédula, nombre, email y contraseña
- **Login**: Iniciar sesión con email y contraseña
- **Homepage**: Panel principal con navegación a todas las aplicaciones

### Gestión de Terrenos (App Terrenos)
- **Agregar Finca**: Registrar nueva finca con ubicación y área total
- **Eliminar Finca**: Eliminar finca y todas sus parcelas asociadas
- **Agregar Parcela**: Registrar parcelas dentro de una finca existente
- **Eliminar Parcela**: Eliminar parcelas específicas
- **Agregar Cultivo**: Registrar cultivos en parcelas
- **Listar**: Ver todas las fincas, parcelas y cultivos del usuario

### Gestión de Maquinaria (App Maquinaria)
- **Mi Maquinaria**: 
  - Agregar nueva maquinaria
  - Eliminar maquinaria propia
  - Ver listado de maquinaria personal
- **Ventas**:
  - Publicar maquinaria para venta
  - Ver maquinaria disponible para compra
  - Solicitar compra de maquinaria ajena
- **Reservas**:
  - Publicar maquinaria para servicio/reserva
  - Ver maquinaria disponible para servicio
  - Solicitar servicio de maquinaria ajena

### Notificaciones (App Notificaciones)
- **Ver Notificaciones**: Lista de todas las notificaciones del usuario
- **Filtros**: Filtrar por tipo y estado (leída/no leída)
- **Eliminar**: Eliminar notificaciones individuales
- **Auto-refresh**: Actualización automática cada 30 segundos

## Comunicación Asíncrona

### Eventos Automáticos
- **Registro de Usuario** → Notificación automática de bienvenida
- **Eliminación de Finca** → Notificación automática al propietario
- **Eliminación de Parcela** → Notificación automática al propietario
- **Publicación de Venta** → Notificación al propietario de la maquinaria
- **Publicación de Servicio** → Notificación al propietario de la maquinaria
- **Interés de Compra** → Notificación al propietario cuando alguien quiere comprar

### Celery Workers
Cada microservicio incluye workers de Celery para procesar tareas asíncronas:
- Envío de notificaciones
- Procesamiento de eventos
- Comunicación entre servicios

## Base de Datos

### Bases de Datos Separadas
- **usuarios_db**: Datos de usuarios y autenticación
- **terrenos_db**: Datos de fincas, parcelas y cultivos
- **maquinaria_db**: Datos de maquinaria, ventas y reservas
- **notificaciones_db**: Datos de notificaciones

### Modelos Principales

#### Usuarios
- `Usuario`: Cédula (PK), nombre, email, contraseña

#### Terrenos
- `Finca`: id_productor + nombre_finca (PK compuesta), ubicación, área_total
- `Parcela`: id_productor + nombre_finca + id_parcela (PK compuesta), área, tipo_suelo
- `Cultivo`: id_productor + nombre_finca + nombre_cultivo (PK compuesta), área, fecha_siembra

#### Maquinaria
- `Maquinaria`: id_maquinaria (PK), propietario, tipo, marca, modelo, año
- `VentaMaquinaria`: id_venta (PK), id_maquinaria, vendedor, comprador, precio
- `ReservaMaquinaria`: id_reserva (PK), id_maquinaria, solicitante, fecha_inicio, fecha_fin

#### Notificaciones
- `Notificacion`: id (PK), id_productor, tipo_notificacion, titulo, mensaje, fecha, prioridad

## API Endpoints

### Usuarios (`/api/usuarios/`)
- `POST /signup/` - Registro de usuario
- `POST /login/` - Login de usuario
- `GET /users/` - Listar usuarios
- `GET /users/{cedula}/` - Obtener usuario específico
- `GET /health/` - Health check

### Terrenos (`/api/terrenos/`)
- `GET /fincas/` - Listar fincas de un productor
- `POST /fincas/agregar/` - Agregar nueva finca
- `DELETE /fincas/eliminar/` - Eliminar finca
- `GET /parcelas/` - Listar parcelas de una finca
- `POST /parcelas/agregar/` - Agregar nueva parcela
- `DELETE /parcelas/eliminar/` - Eliminar parcela
- `GET /cultivos/` - Listar cultivos
- `POST /cultivos/agregar/` - Agregar nuevo cultivo
- `GET /health/` - Health check

### Maquinaria (`/api/maquinaria/`)
- `GET /maquinaria/` - Listar maquinaria de un propietario
- `POST /maquinaria/crear/` - Crear nueva maquinaria
- `DELETE /maquinaria/{id}/eliminar/` - Eliminar maquinaria
- `GET /ventas/` - Listar ventas disponibles
- `POST /ventas/crear/` - Crear nueva venta
- `GET /reservas/` - Listar reservas disponibles
- `POST /reservas/crear/` - Crear nueva reserva
- `GET /health/` - Health check

### Notificaciones (`/api/notificaciones/`)
- `GET /notificaciones/` - Listar notificaciones de un usuario
- `POST /notificaciones/crear/` - Crear nueva notificación
- `DELETE /notificaciones/{id}/eliminar/` - Eliminar notificación
- `GET /health/` - Health check

## Comandos Útiles

### Gestión de Contenedores
```bash
# Ver estado de todos los servicios
docker compose ps

# Ver logs de todos los servicios
docker compose logs

# Ver logs de un servicio específico
docker compose logs usuarios
docker compose logs terrenos
docker compose logs maquinaria
docker compose logs notificaciones

# Ver logs en tiempo real
docker compose logs -f

# Reiniciar un servicio específico
docker compose restart usuarios

# Detener todos los servicios
docker compose down

# Detener y eliminar volúmenes (CUIDADO: elimina datos)
docker compose down -v
```

### Ejecutar Comandos Dentro de Contenedores
```bash
# Acceder al shell de un microservicio
docker compose exec usuarios python manage.py shell
docker compose exec terrenos python manage.py shell
docker compose exec maquinaria python manage.py shell
docker compose exec notificaciones python manage.py shell

# Acceder a la base de datos PostgreSQL
docker compose exec postgres psql -U farm_user -d usuarios_db
docker compose exec postgres psql -U farm_user -d terrenos_db
docker compose exec postgres psql -U farm_user -d maquinaria_db
docker compose exec postgres psql -U farm_user -d notificaciones_db

# Crear superusuario para Django Admin
docker compose exec usuarios python manage.py createsuperuser
docker compose exec terrenos python manage.py createsuperuser
docker compose exec maquinaria python manage.py createsuperuser
docker compose exec notificaciones python manage.py createsuperuser
```

### Gestión de Migraciones
```bash
# Ejecutar migraciones
docker compose exec usuarios python manage.py migrate
docker compose exec terrenos python manage.py migrate
docker compose exec maquinaria python manage.py migrate
docker compose exec notificaciones python manage.py migrate

# Crear nuevas migraciones (desarrollo)
docker compose exec usuarios python manage.py makemigrations
docker compose exec terrenos python manage.py makemigrations
docker compose exec maquinaria python manage.py makemigrations
docker compose exec notificaciones python manage.py makemigrations
```

### Gestión de Celery
```bash
# Ver logs de workers de Celery
docker compose logs usuarios-worker
docker compose logs terrenos-worker
docker compose logs maquinaria-worker
docker compose logs notificaciones-worker

# Reiniciar workers
docker compose restart usuarios-worker
docker compose restart terrenos-worker
docker compose restart maquinaria-worker
docker compose restart notificaciones-worker
```

## Solución de Problemas

### Problema: Servicios no inician
```bash
# Verificar logs de errores
docker compose logs

# Verificar que Docker esté funcionando
docker ps

# Verificar que los puertos estén libres
netstat -tuln | grep -E ':(80|8001|8002|8003|8004|5432|5672|15672)'
```

### Problema: Base de datos no conecta
```bash
# Verificar que PostgreSQL esté funcionando
docker compose logs postgres

# Verificar conectividad
docker compose exec postgres pg_isready -U farm_user -d usuarios_db
```

### Problema: RabbitMQ no conecta
```bash
# Verificar que RabbitMQ esté funcionando
docker compose logs rabbitmq

# Verificar conectividad
docker compose exec rabbitmq rabbitmq-diagnostics ping
```

### Problema: Migraciones fallan
```bash
# Eliminar migraciones y recrearlas
docker compose exec usuarios python manage.py migrate --fake-initial
docker compose exec terrenos python manage.py migrate --fake-initial
docker compose exec maquinaria python manage.py migrate --fake-initial
docker compose exec notificaciones python manage.py migrate --fake-initial
```

### Problema: Frontend no carga
```bash
# Verificar que Nginx esté funcionando
docker compose logs nginx

# Verificar que los archivos estén en el lugar correcto
docker compose exec nginx ls -la /usr/share/nginx/html
```

## Estructura del Proyecto
```
bbb/
├── docker-compose.yml          # Orquestación principal de servicios
├── docker-compose-simple.yml   # Orquestación simplificada
├── start.sh                    # Script de inicio principal
├── start-fast.sh               # Script de inicio rápido
├── init-db.sql                 # Script de inicialización de bases de datos
├── nginx/
│   └── nginx.conf             # Configuración de Nginx
├── frontend/
│   ├── index.html             # Página principal
│   ├── terrenos.html          # Gestión de terrenos
│   ├── maquinaria.html        # Gestión de maquinaria
│   ├── notificaciones.html    # Notificaciones
│   ├── agregar-finca.html     # Formulario agregar finca
│   ├── agregar-cultivo.html   # Formulario agregar cultivo
│   ├── agregar-maquinaria.html # Formulario agregar maquinaria
│   ├── agregar-notificacion.html # Formulario agregar notificación
│   ├── styles.css             # Estilos CSS
│   └── app.js                 # JavaScript principal
├── usuarios/                   # Microservicio de usuarios
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── startup.sh
│   ├── manage.py
│   ├── usuarios/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   └── usuarios_app/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── tasks.py
├── terrenos/                   # Microservicio de terrenos
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── startup.sh
│   ├── manage.py
│   ├── terrenos/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   └── terrenos_app/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── tasks.py
├── maquinaria/                 # Microservicio de maquinaria
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── startup.sh
│   ├── manage.py
│   ├── maquinaria/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   └── maquinaria_app/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── tasks.py
└── notificaciones/             # Microservicio de notificaciones
    ├── Dockerfile
    ├── requirements.txt
    ├── startup.sh
    ├── manage.py
    ├── notificaciones/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── celery.py
    └── notificaciones_app/
        ├── models.py
        ├── views.py
        ├── serializers.py
        ├── urls.py
        └── tasks.py
```

## Características Técnicas

### Tecnologías Utilizadas
- **Backend**: Django 4.x, Django REST Framework
- **Base de Datos**: PostgreSQL 15
- **Message Broker**: RabbitMQ 3.12
- **Task Queue**: Celery
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Proxy**: Nginx
- **Containerización**: Docker, Docker Compose
- **Arquitectura**: Microservicios SOA

### Características de Seguridad
- Autenticación por email y contraseña
- Validación de datos en frontend y backend
- Sanitización de inputs
- Headers de seguridad en Nginx

### Características de Escalabilidad
- Arquitectura de microservicios
- Bases de datos separadas por servicio
- Comunicación asíncrona con RabbitMQ
- Workers de Celery para tareas pesadas
- Proxy reverso con Nginx

## Soporte

Si encuentras problemas al ejecutar el sistema:

1. **Verifica los prerrequisitos**: Docker y Docker Compose instalados
2. **Revisa los logs**: `docker compose logs`
3. **Verifica los puertos**: Asegúrate de que no haya conflictos
4. **Reinicia los servicios**: `docker compose restart`
5. **Consulta la documentación**: Revisa este README completo

## Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente para fines educativos y comerciales. 