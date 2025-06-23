-- Script de inicialización de bases de datos para microservicios
-- Este script crea las bases de datos separadas para cada microservicio

-- Crear base de datos para usuarios
CREATE DATABASE usuarios_db;

-- Crear base de datos para terrenos
CREATE DATABASE terrenos_db;

-- Crear base de datos para maquinaria
CREATE DATABASE maquinaria_db;

-- Crear base de datos para notificaciones
CREATE DATABASE notificaciones_db;

-- Crear base de datos para la granja
CREATE DATABASE farm_db;

-- Otorgar permisos al usuario farm_user en todas las bases de datos
GRANT ALL PRIVILEGES ON DATABASE usuarios_db TO farm_user;
GRANT ALL PRIVILEGES ON DATABASE terrenos_db TO farm_user;
GRANT ALL PRIVILEGES ON DATABASE maquinaria_db TO farm_user;
GRANT ALL PRIVILEGES ON DATABASE notificaciones_db TO farm_user; 