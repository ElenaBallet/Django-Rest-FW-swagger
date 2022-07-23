# Django-Rest-FW-swagger
Руководство по созданию API средствами DRF и swagger. Сайт разработан на основании статьи: https://appliku.com/post/django-rest-framework-swagger-and-typescript-api-c

## Этапы построения API

### 1. Установить необходимые библиотеки

```python 
pip install -r requirements.txt
```

### 2. Создать проект джанго

```python 
django-admin startproject django_api .
```

### 3. Создать приложение myapi (ветка app_myapi)

```python 
python3 manage.py startapp myapi
```

### 4. Создать суперпользователя

```python 
python3 manage.py createsuperuser
```
