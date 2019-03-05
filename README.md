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

#3. Run Docker
```
	docker-compose up
```