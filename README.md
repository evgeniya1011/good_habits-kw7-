Сервис Полезных привычек

Настройки проекта:
1)Активировать виртуальное окружение
source venv/bin/activate
2)Установить зависимости проекта, указанные в файле requirements.txt
pip install -r requirements.txt
3)Установка и запуск Redis
pip install redis
sudo apt-get install redis-server
sudo service redis-server start

4)Создать базу данных в PostreSQL
CREATE DATABASE dbname;
5)Применить миграции
6)Запустить сервер
python manage.py runserver
6)Запустить Celery
celery -A config worker -l INFO
celery -A config beat -l info -S django

Задачи:
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Проект разработан с использованием концепции, описанной в данной книге.

Модели
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше 2 минут.

Валидация
Исключены одновременный выбор связанной привычки и указания вознаграждения.
Время выполнения должно быть не больше 120 секунд.
В связанные привычки могут попадать только привычки с признаком приятной привычки.
У приятной привычки не может быть вознаграждения или связанной привычки.
Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

Права доступа
Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

Отложенные задачи
Для полноценной работы сервиса реализована работа с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.

Для этого сделана интеграция сервиса с мессенджером Telegram, который будет заниматься рассылкой уведомлений.

Безопасность
Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

Документация
Для реализации экранов настроен вывод документации.

В проекте используется Docker Compose

Для запуска приложения необходимо выполнить следующие команды: docker-compose build - сборка образа docker-compose up - заупск контейнера

Если БД не создана, то необходимо будет ее создать, но перед этим убедиться, что у вас запущен контейнер. Команда для создания БД: docker-compose exec db psql -U postgres

