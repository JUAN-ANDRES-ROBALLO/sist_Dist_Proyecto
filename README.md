# Proyecto SOA de Gestión Agrícola

Este sistema distribuye 4 apps Django usando RabbitMQ, PostgreSQL, y NGINX como proxy.

## Estructura

- usuarios/
- terrenos/
- maquinaria/
- notificaciones/
- nginx/
- docker-compose.yml

## Levantar el sistema

```
docker compose up --build
```

## Acceso

- Usuarios: http://localhost/usuarios/
- Terrenos: http://localhost/terrenos/
- Maquinaria: http://localhost/maquinaria/
- Notificaciones: http://localhost/notificaciones/