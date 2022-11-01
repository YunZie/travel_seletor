# [Project Introduce](https://www.linkedin.com/pulse/%E8%BF%BD%E5%85%89%E8%80%85%E5%BE%9E%E4%BB%8B%E9%9D%A2%E8%A8%AD%E8%A8%88%E8%90%BD%E5%AF%A6%E5%88%B0%E5%89%8D%E5%BE%8C%E7%AB%AF%E8%88%87%E7%AB%B6%E8%B3%BD%E9%81%8E%E7%A8%8B-su-huan-chen/)

# Build this project
```bash
Install [docker](https://www.docker.com/products/docker-desktop/)

python manage.py makemigrations
python manage.py migrate
```

# start
```bash
python manage.py runserver
```

# Deploy in running
```
docker-compose run web python manage.py migrate

python manage.py runserver
```
