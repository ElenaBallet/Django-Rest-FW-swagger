# Django-Rest-FW-swagger
Руководство по созданию API средствами DRF и swagger. Сайт разработан на основании статьи: https://appliku.com/post/django-rest-framework-swagger-and-typescript-api-c

## Шаги построения API

### 1. Установите необходимые библиотеки

```python 
pip install -r requirements.txt
```

### 2. Создайте проект джанго

```python 
django-admin startproject django_api .
```

### 3. Создаем приложение myapi

```python 
python3 manage.py startapp myapi
```

### 4. Клонируйте ветку app_myapi

```python 
git clone --single-branch --branch app_myapi git@github.com:ElenaBallet/Django-Rest-FW-swagger.git
```

### 5. Создайте суперпользователя

```python 
python3 manage.py createsuperuser
```
