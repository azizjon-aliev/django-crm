#!/usr/bin/bash

set -o errexit
set -o nounset

# Check env variables
echo "DJANGO_ENV is ${DJANGO_ENV}"
echo "Port 8000 exposed for Django CRM"

# Set working directory
cd ${PROJECT_DIR}
echo "Change to working directory $(pwd)"

## Run database migrations
python manage.py migrate
python manage.py collectstatic --no-input

mkdir -p media static
chmod -R 755 media static

if [ ${DJANGO_ENV} = 'development' ]; then
    # Start API server
    python manage.py init_admin
    python manage.py add_default_groups
    python manage.py loaddata db.json
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn src.config.wsgi --bind 0.0.0.0:8000
fi