install
"""
python manage.py makemigrations
python manage.py migrate
"""


start run
"""
python manage.py runserver
"""

start first deploy
"""
docker-compose run web python manage.py migrate

python manage.py runserver
"""