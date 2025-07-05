#!/bin/sh

# Wait for PostgreSQL port to be open
until nc -z db 5432; do
  echo "Waiting for Postgres..."
  sleep 2
done

echo "Postgres is up!"
exec "$@"
