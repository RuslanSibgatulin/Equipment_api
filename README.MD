# Equipment_api - каталог оборудования.
![CI](https://github.com/RuslanSibgatulin/Equipment_api/actions/workflows/test.yml/badge.svg)

API-сервис, поволяющий хранить список оборудования в строгом соответствии с шаблоном серийного номера.

## Используемые технологии
- Код приложения на Python
- Фреймворк [Django 4](https://docs.djangoproject.com/en/4.1/) + [DRF](https://www.django-rest-framework.org/#installation)
- Swagger документация [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/index.html)
- СУБД - MySql
- Фронтенд на фреймворке [Vue.js 3](https://v3.ru.vuejs.org/ru/guide/introduction.html)
- Все компоненты системы запускаются через Docker-compose.

# Запуск приложения
## Клонировать репозиторий
    git clone https://github.com/RuslanSibgatulin/Equipment_api.git

## Переменные окружения
Подготовить файл с переменными окружения по аналогии с файлом `docker/envs/*.example` и пересохранить в файл `*.env`

## Запуск
    make start

### При первичном запуске необходимо выполнить команды инициализации
    make init

## Функционал
- [Фронтенд Vue3](http://127.0.0.1/)
- [Админ-панель](http://127.0.0.1/admin/)
- [OpenAPI документация](http://127.0.0.1/apidocs/)
