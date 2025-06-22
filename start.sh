#!/bin/bash

echo "🚀 Iniciando Sistema de Gestión Agrícola SOA..."
echo "================================================"

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Por favor instala Docker primero."
    exit 1
fi

# Verificar si Docker Compose está disponible
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose no está disponible. Por favor instala Docker Compose."
    exit 1
fi

# Verificar puertos disponibles
echo "🔍 Verificando puertos disponibles..."

PORTS=(80 8001 8002 8003 8004 5432 5672 15672 6379)
for port in "${PORTS[@]}"; do
    if netstat -tuln | grep ":$port " > /dev/null; then
        echo "⚠️  Puerto $port está en uso. Asegúrate de que no haya conflictos."
    fi
done

echo ""
echo "📦 Construyendo y levantando servicios..."

# Usar docker compose si está disponible, sino docker-compose
if docker compose version &> /dev/null; then
    COMPOSE_CMD="docker compose"
else
    COMPOSE_CMD="docker-compose"
fi

# Levantar servicios
$COMPOSE_CMD up --build -d

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Sistema iniciado exitosamente!"
    echo ""
    echo "🌐 Accesos:"
    echo "   • Frontend Principal: http://localhost"
    echo "   • RabbitMQ Management: http://localhost:15672"
    echo "     (Usuario: farm_user, Contraseña: farm_password)"
    echo ""
    echo "📊 Verificar servicios:"
    echo "   • $COMPOSE_CMD ps"
    echo "   • $COMPOSE_CMD logs -f"
    echo ""
    echo "🛑 Para detener el sistema:"
    echo "   • $COMPOSE_CMD down"
    echo ""
    echo "🎉 ¡Disfruta tu sistema SOA!"
else
    echo ""
    echo "❌ Error al iniciar el sistema."
    echo "📋 Revisa los logs con: $COMPOSE_CMD logs"
    exit 1
fi 