#! /usr/bin/env sh
set -e

export APP_MODULE="api:app"
export GUNICORN_CONF=/app/config/gunicorn_conf.py

. /app/source/scripts/prestart.sh

exec gunicorn -k uvicorn.workers.UvicornWorker -c "$GUNICORN_CONF" "$APP_MODULE"
