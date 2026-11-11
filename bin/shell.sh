
cd "$(dirname "$0")/../backend" || exit

docker compose exec django python manage.py shell