#! /usr/bin/env sh
set -e

. /app/scripts/prestart.sh

exec gunicorn -k uvicorn.workers.UvicornWorker -c $GUNICORN_CONF $APP_MODULE
