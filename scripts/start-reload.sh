#! /usr/bin/env sh
set -e

. /app/scripts/prestart.sh

exec uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL $APP_MODULE
