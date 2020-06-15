echo "Running migrations"
alembic -c /app/source/alembic/alembic.ini upgrade head
echo "Finished migrations"
