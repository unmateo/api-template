#! /usr/bin/env sh
set -e

export APP_MODULE="api:app"
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-80}
LOG_LEVEL=${LOG_LEVEL:-info}

. /app/scripts/prestart.sh

exec uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL "$APP_MODULE"
