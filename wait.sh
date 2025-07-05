#!/bin/sh

# Wait until FastAPI is available
echo "Waiting for FastAPI service..."
until nc -z web 8000; do
  sleep 2
done

echo "FastAPI is up. Starting Nginx..."
nginx -g "daemon off;"
