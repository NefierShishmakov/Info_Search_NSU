Приложение тестировалось на Ubuntu 22.04 с python 3.10.12 БД - postgresql 15

Что необходимо для запуска: python3, pip, python3-venv

Установка:
1. Заходим в корневую директорию репозитория и выполняем команду в терминале: python3 -m venv flaskenv
2. Выполняем команду в терминале: source flaskenv/bin/activate
3. Выполняем команду в терминале: pip install -r requirements.txt
4. Создаём файл в корневой директории .env со следующими значениями:
FLASK_SQLALCHEMY_DATABASE_URI="postgresql://username:password@localhost:5432/database_name" - username, password, database_name пишем свои
FLASK_SQLALCHEMY_TRACK_MODIFICATIONS=False
FLASK_CSRF_ENABLED=True
FLASK_SECRET_KEY="сюда пишем абсолютно любую строку"
5. Выполняем команду в терминале(Перед этим вам нужно создать пользователя с базой данных): flask db init && flask db migrate && flask db upgrade
6. Запускаем: flask run
7. Переходим в браузер по адресу: localhost:5000

P.S. При каждом запуске командной оболочки нужно делать 2-ой шаг.
