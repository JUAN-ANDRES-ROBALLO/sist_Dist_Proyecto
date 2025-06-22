#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! pg_isready -h postgres -p 5432 -U farm_user -d terrenos_db; do
    sleep 2
done
echo "Database is ready!"

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Start the application
echo "Starting terrenos service..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 terrenos.wsgi:application 