# django_rest_template
Dockerize Django RESTFull Template


# STEPS
#1. Build Docker
```
	docker-compose build
```

#2. Generate Django Project
```
	docker-compose run web django-admin startproject [PROJECT_NAME] .
```

#2.1 Create App on Django Project
```
	docker-compose run web python manage.py startapp [FEATURE_NAME]
```

#3. Run Docker
```
	docker-compose up
```
#4. Create Migration With Alembic (If you don't want to use standard ORM)
```
	docker-compose run web alembic init --templaet generic alembic
```
#4.1 Change the sql driver in alembic.ini
```
	sqlalchemy.url = mysql://root:@localhost/database_name
```
#4.2 Create Migration using alembic
```
	docker-compose run web alembic revision -m "[TEXT]"
```
#4.2 Migrate file
```
	docker-compose run web alembic upgrade head
```
