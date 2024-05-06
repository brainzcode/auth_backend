#!/bin/sh

if [ -z "$SQL_HOST" ] || [ -z "$DATABASE" ]; then
  echo "Error: SQL_HOST and DATABASE environment variables are not set."
  exit 1
fi

if [ "$DATABASE" = "postgres" ] 
then
    echo "Check if database is running..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        echo "Database not yet available, waiting..."
        sleep 0.1
        if [ $? -ne 0 ]; then
          echo "Error: Failed to connect to database."
          exit 1
        fi
    done

    echo "The database is up and running :)"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"
