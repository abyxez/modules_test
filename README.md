git clone 

cd modules_test/

Cоздать и активировать виртуальное окружение:

python3 -m venv env

source venv/bin/activate (macOS)

or 

source venv/Scripts/activate ( WIN )

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Выполнить миграции:

cd modules/

python3 manage.py makemigrations

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver

-------

Этот проект представляет собой простой API сервис с возможностью добавления Образовательных модулей. Например, если выполнить команду

python3 manage.py createsuperuser

и пройти по адресу:

127.0.0.1:8000/admin/

В админке можно добавить любые модули, которые далее будут доступны с помощью API сервиса, например, Postman, уже по адресу:

127.0.0.1:8000/api/v1/titles/ - GET method

