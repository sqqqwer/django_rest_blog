# API YATUBE
API для Yatube на Django REST freamwork с JWT аутентификацией.

## Содержание
- [Установка и запуск](#установка-и-запуск)
- [Документация](#документация)
- [Примеры запросов](#примеры-запросов)
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
$ cd blogicum/
```

```bash
$ python manage.py runsrever
```

## Документация
Для просмотра документации запустите проект локально и прейдите по адресу http://127.0.0.1:8000/redoc/


## Примеры запросов
|Http-метод|Эндпоинт|Параметры|Требуется токен|Результат|
| :-: | :-- | :-: | :-: | - |
| GET | api/v1/posts/?limit=2&offset=4 | —— |:x:| Получение 2 постов с 3 страницы |
| GET | api/v1/posts/3/comments/ | —— |:x:| Получение **всех** комментариев с поста с id 3 |
| POST | api/v1/jwt/verify/ | Обязательно: username и password существующего пользователя | :x: | Получение аунтефикационного токена |
| POST | api/v1/posts/ | Обязательно: text |:heavy_check_mark:| Создание поста |

Подробнее см. [Документацию](#документация)




