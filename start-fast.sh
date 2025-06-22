#!/bin/bash

echo "🚀 Iniciando Sistema Agrícola SOA (Versión Rápida)..."
echo "================================================"

# Detener contenedores existentes
echo "🛑 Deteniendo contenedores existentes..."
docker compose -f docker-compose-simple.yml down

# Limpiar imágenes no utilizadas (opcional)
echo "🧹 Limpiando imágenes no utilizadas..."
docker system prune -f

# Construir e iniciar servicios
echo "📦 Construyendo e iniciando servicios..."
docker compose -f docker-compose-simple.yml up --build -d

# Esperar a que los servicios estén listos
echo "⏳ Esperando a que los servicios estén listos..."
sleep 30

# Verificar estado de los servicios
echo "🔍 Verificando estado de los servicios..."
docker compose -f docker-compose-simple.yml ps

echo ""
echo "🎉 ¡Sistema iniciado exitosamente!"
echo ""
echo "📋 URLs de acceso:"
echo "   🌐 Frontend: http://localhost"
echo "   👥 Usuarios API: http://localhost:8001"
echo "   🌾 Terrenos API: http://localhost:8002"
echo "   🚜 Maquinaria API: http://localhost:8003"
echo "   🔔 Notificaciones API: http://localhost:8004"
echo "   🐰 RabbitMQ Management: http://localhost:15672"
echo ""
echo "📝 Credenciales:"
echo "   - Usuario: farm_user"
echo "   - Contraseña: farm_password"
echo ""
echo "🛑 Para detener: docker compose -f docker-compose-simple.yml down" 