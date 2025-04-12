# Django Rest Blog
API на Django Rest
Этот проект представляет собой REST API для блога, с помощью которого пользователи могут взаимодействовать с платформой. Основные возможности API включают:
- Создание и управление публикациями, а также добавление и редактирование комментариев к ним.
- Система пользователей с возможностью подписки на других авторов.
- Админ-панель, которая позволяет создавать и редактировать категории публикаций для более удобной организации контента.

API поддерживает JWT аутентификацию пользователей и построен с учетом удобства использования и гибкости для расширения функционала блога.

## Содержание
- [Установка и запуск](#установка-и-запуск)
- [Документация](#документация)
- [Стек технологий](#стек-технологий)
- [Примеры запросов](#примеры-запросов)
- [Авторство](#авторство)

## Установка и запуск
1. Клонирование репозитория
   
```bash
$ git clone https://github.com/sqqqwer/api_final_yatube.git
```

2. Переход в директорию проекта

```bash
$ cd api_final_yatube
```

3. Создание виртуального окружения

```bash
$ python -m venv venv
```

4. Активация виртуального окружения

- Если Windows:
```bash
$ . venv/Scripts/activate
```
- Если Linux/macOS:
```bash
$ . venv/bin/activate
```
5. Установка зависимостей

```bash
$ pip install -r requirements.txt
```

6. **_Локальный запуск проекта_**

```bash
$ cd yatube_api/
```

```bash
$ python manage.py runsrever
```

## Документация
Для просмотра документации запустите проект локально и прейдите по адресу http://127.0.0.1:8000/redoc/

## Стек технологий
Python, Django, Django rest framework, SQLite
Аунтефикация: PyJWT, Simple JWT, djoser
Тесты: pytest
Документация: ReDoc


## Примеры запросов
#### Получение 2 постов с 3 страницы
**Запрос:**
```
GET http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4
```
**Ответ:**
```
HTTP/1.1 200 OK
Content-Type: application/json
{
  "count": 26,
  "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=6",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
  "results": [
    {
      "id": 22,
      "author": "Автор1",
      "text": "Текст поста",
      "pub_date": "2024-10-27T06:54:49.800181Z",
      "image": null,
      "group": 2
    },
    {
      "id": 21,
      "author": "Автор2",
      "text": "Текст поста",
      "pub_date": "2024-10-27T06:54:49.658056Z",
      "image": null,
      "group": 0
    }
  ]
}
```

#### Получение всех комментариев с поста с id 3
**Запрос:**
```
GET http://127.0.0.1:8000/api/v1/posts/3/comments/
```
**Ответ:**
```
HTTP/1.1 200 OK
Content-Type: application/json
[
  {
      "id": 3,
      "author": "Автор1",
      "text": "Тест комментарий 1",
      "created": "2024-10-30T06:23:52.889931Z",
      "post": 3
    },
    {
      "id": 4,
      "author": "Автор2",
      "text": "Тест комментарий 2",
      "created": "2024-10-30T06:23:54.981596Z",
      "post": 3
    },
    {
      "id": 5,
      "author": "Автор2",
      "text": "Тест комментарий 3",
      "created": "2024-10-30T06:23:56.756929Z",
      "post": 3
    }
]
```

#### Получение аунтефикационного токена
**Запрос:**
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "Автор1",
    "password": "123"
}
```
**Ответ:**
```
HTTP/1.1 200 OK
Content-Type: application/json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDM1NzE2NCwiaWF0IjoxNzMwMjcwNzY0LCJqdGkiOiJkMzg0MzZjM2IzZDQ0YTA0ODNjY2JkZGY4YjM2Y2Y3MyIsInVzZXJfaWQiOjJ9.qh61jo_5SanDKKB9WRe5rD8E0Sp2bTOw1FHKqhmPHSw",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMzU3MTY0LCJpYXQiOjE3MzAyNzA3NjQsImp0aSI6IjY3OTkxZTk3N2Q0MTRhODk4N2RjZjkxM2FmNDhlYjVmIiwidXNlcl9pZCI6Mn0.m54KyW1-6f8cv1KdPFzAdwLSlOnzJbxGuqa_J6hSOGA"
}
```

#### Создание поста
**Запрос:**
```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMzU3MTY0LCJpYXQiOjE3MzAyNzA3NjQsImp0aSI6IjY3OTkxZTk3N2Q0MTRhODk4N2RjZjkxM2FmNDhlYjVmIiwidXNlcl9pZCI6Mn0.m54KyW1-6f8cv1KdPFzAdwLSlOnzJbxGuqa_J6hSOGA

{
    "text": "Текст поста.",
    "group": 1
}
```
**Ответ:**
```
HTTP/1.1 201 Created
Content-Type: application/json
{
  "id": 29,
  "author": "Автор1",
  "text": "Текст поста.",
  "pub_date": "2024-10-30T06:43:55.300952Z",
  "image": null,
  "group": 1
}
```

##### Подробнее см. [Документацию](#документация)

## Авторство
Учебный проект сделал Владислав Чернявский (sqqqwer) на основе форка Яндекс Практикума.
