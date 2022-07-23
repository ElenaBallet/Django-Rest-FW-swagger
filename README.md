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

### 5. Настроить swagger (ветка create_swagger)

### 6. Создать приложение React и сгенерировать TypeScript API Client из swagger.json

#### 6.1.1 На всякий случай удалим предыдущую версию create-react-app:

```
npm uninstall -g create-react-app
```

#### 6.1.2 Создадим приложение React:

```
npx create-react-app swagger-api-demo --template typescript
cd swagger-api-demo
```

#### 6.1.3 Установим OpenAPI Typescript Codegen:

```
npm install -g openapi-typescript-codegen
```

#### 6.1.4 Генерация API клиента:

```
wget http://127.0.0.1:8000/swagger.json -O swagger.json && openapi  --input ./swagger.j
```

#### 6.1.5 Запуск сервера http://localhost:3000/:

```
npm start
```

