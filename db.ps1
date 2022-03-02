$make_migrations = "python manage.py makemigrations articles"
$migrate = "python manage.py migrate"

iex $make_migrations
iex $migrate