#!/bin/bash
set -e

echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Crear superusuario si las variables están definidas
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Creando superusuario..."
    python manage.py createsuperuser --noinput 2>/dev/null || echo "Superusuario ya existe."
fi

echo "Iniciando Gunicorn..."
exec gunicorn proyecto.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120
